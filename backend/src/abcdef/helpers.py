import logging
import os
import requests
import pandas as pd
import traceback
from typing import Generator, List
from django.conf import settings
from django.db import connections, transaction
from psycopg2.extras import execute_values
from abcdef import models as abcdef_models


logger = logging.getLogger('celery')
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3029.110 Safari/537.36'
}


def write_file(file_name: str, content: str, mode='w'):
    while True:
        try:
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            with open(file_name, mode) as f1:
                # fcntl.flock(f1, fcntl.LOCK_EX | fcntl.LOCK_NB)
                f1.write(content)
                # fcntl.flock(f1, fcntl.LOCK_UN)
            break
        except Exception:
            raise


def get_files(exists_only=False) -> Generator[str, str, str]:
    # TODO: сделать парсер c сайта, с проверкой на необходимость скачивания файла
    # если каждый день меняется и там timestamp реальный (сейчас 24 год)
    for link in [
        'https://opendata.digital.gov.ru/downloads/ABC-3xx.csv',
        'https://opendata.digital.gov.ru/downloads/ABC-4xx.csv',
        'https://opendata.digital.gov.ru/downloads/ABC-8xx.csv',
        'https://opendata.digital.gov.ru/downloads/DEF-9xx.csv',
        # 'https://opendata.digital.gov.ru/downloads/ABC-3xx.csv?1710948258581',
        # 'https://opendata.digital.gov.ru/downloads/ABC-4xx.csv?1710948258582',
        # 'https://opendata.digital.gov.ru/downloads/ABC-8xx.csv?1710948258582',
        # 'https://opendata.digital.gov.ru/downloads/DEF-9xx.csv?1710948258583',
    ]:
        base_name = os.path.basename(link)  # .split('?')[0]
        file_name = os.path.join(settings.FILES_ROOT, base_name)
        if os.path.exists(file_name):
            if exists_only:
                yield link, file_name, base_name
        else:
            if not exists_only:
                yield link, file_name, base_name


def log_info(file_base_name: str, params: dict) -> None:
    abcdef_models.DownloadInfo.objects.update_or_create(
        name=file_base_name,
        defaults=params,
    )


def download_file(link: str, file_name: str, base_name: str, try_count: int) -> bool:
    req = requests.get(link, headers=headers)
    if req.status_code != 200:
        logger.error(f'Failed to download file {base_name} {link}')
        log_info(file_base_name=base_name, params={
            'link': link,
            'is_downloaded': False,
            'is_added': False,
            'retry_count': try_count,
            'status_message': f'Failed to download file {base_name} {link}',
        })
        return False
    write_file(
        file_name,
        req.content,
        mode='wb'
    )
    log_info(file_base_name=base_name, params={
        'link': link,
        'is_downloaded': True,
        'is_added': False,
        'retry_count': try_count,
        'status_message': '',
    })
    return True


@transaction.atomic
def batch_update(table_name: str,
                 data: List[list],
                 col_keys: List[str],
                 col_upd: List[str],
                 col_names: List[str],
                 conflict_res: str = 'UPDATE',  # IGNORE
                 ) -> None:
    with connections['default'].cursor() as cursor:
        if len(data):
            if 'UPDATE' == conflict_res:
                updates = ','.join([
                    f'{f} = excluded.{f}' for f in col_upd
                ])
                tmpl = f'''
                INSERT INTO {table_name} ({','.join(col_names)})
                VALUES %s
                ON CONFLICT ({','.join(col_keys)}) DO UPDATE
                SET {updates} ;'''
            else:
                tmpl = f'''
                INSERT INTO {table_name} ({','.join(col_names)})
                VALUES %s
                ON CONFLICT ({','.join(col_keys)}) DO NOTHING ; '''

            execute_values(cursor, tmpl, data)


def process_files_all() -> None:
    for _, file_name, base_name in get_files(True):
        process_file(file_name, base_name)


def process_file(file_name, base_name) -> None:
    try:
        df = pd.read_csv(file_name, sep=';', dtype=str)
        # название первой колонки кривое в файлах
        df = df.set_axis('АВС/ DEF;От;До;Емкость;Оператор;Регион;Территория ГАР;ИНН'.split(';'), axis='columns')
        # АВС/ DEF;От;До;Емкость;Оператор;Регион;Территория ГАР;ИНН

        data = df.to_records(index=False).tolist()
        batch_update(
            table_name=abcdef_models.Phone._meta.db_table,
            data=data,
            col_keys=['num_prefix', 'num_start', 'num_end'],
            col_upd=['capacity', 'opsos', 'region', 'territory', 'inn'],
            col_names=['num_prefix', 'num_start', 'num_end', 'capacity', 'opsos', 'region', 'territory', 'inn'],
        )

        df_opsos = df[['Оператор']].drop_duplicates()
        batch_update(
            table_name=abcdef_models.Opsos._meta.db_table,
            data=df_opsos.to_records(index=False).tolist(),
            col_keys=['name'],
            col_upd=['name'],
            col_names=['name'],
        )

        df_ter = df[['Территория ГАР']].drop_duplicates()
        batch_update(
            table_name=abcdef_models.Territory._meta.db_table,
            data=df_ter.to_records(index=False).tolist(),
            col_keys=['name'],
            col_upd=['name'],
            col_names=['name'],
        )

        pred = [{'Оператор-ID': o.id, 'Оператор': o.name} for o in abcdef_models.Opsos.objects.all()]
        df_opsos = pd.DataFrame(pred)
        pred = [{'Территория ГАР-ID': o.id, 'Территория ГАР': o.name} for o in abcdef_models.Territory.objects.all()]
        df_ter = pd.DataFrame(pred)

        df_norm = df['АВС/ DEF;От;До;Емкость;Оператор;Регион;Территория ГАР;ИНН'.split(';')]
        df_norm = pd.merge(df_norm, df_opsos, how='left', on='Оператор')
        df_norm = pd.merge(df_norm, df_ter, how='left', on='Территория ГАР')
        df_norm['num_min'] = df_norm['АВС/ DEF'] + df_norm['От']
        df_norm['num_max'] = df_norm['АВС/ DEF'] + df_norm['До']
        df_norm = df_norm.astype({'num_max': str, 'num_min': str})
        df_norm = df_norm['АВС/ DEF;num_min;num_max;Емкость;Оператор-ID;Территория ГАР-ID;ИНН'.split(';')]

        data_norm = df_norm.to_records(index=False).tolist()
        batch_update(
            table_name=abcdef_models.PhoneNorm._meta.db_table,
            data=data_norm,
            col_keys=['num_min', 'num_max'],
            col_upd=['num_prefix', 'capacity', 'opsos_id', 'territory_id', 'inn'],
            col_names=['num_prefix', 'num_min', 'num_max', 'capacity', 'opsos_id', 'territory_id', 'inn'],
        )
        log_info(file_base_name=base_name, params={
            'is_downloaded': False,
            'is_added': True,
            'status_message': '',
        })
    except Exception:
        logger.error(traceback.format_exc())
        log_info(file_base_name=base_name, params={
            'is_added': False,
            'status_message': traceback.format_exc(),
        })
