import logging
import os
import requests
import pandas as pd
from typing import Generator, List
from django.conf import settings
from django.db import connections, transaction
from psycopg2.extras import execute_values
from abcdef.models.phone import Phone


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


def download_file(link: str, file_name: str, base_name: str) -> bool:
    # TODO: возможно надо selenium-ом скачивать, а то там какая-то минимальная
    # защита по UserAgent уже есть, вдруг еще добавят
    req = requests.get(link, headers=headers)
    if req.status_code != 200:
        logger.error(f'Failed to download file {base_name} {link}')
        return False
    write_file(
        file_name,
        req.content,
        mode='wb'
    )
    return True


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
    df = pd.read_csv(file_name, sep=';', dtype=str)
    # АВС/ DEF;От;До;Емкость;Оператор;Регион;Территория ГАР;ИНН
    data = df.to_records(index=False).tolist()
    batch_update(
        table_name=Phone._meta.db_table,
        data=data,
        col_keys=['num_prefix', 'num_start', 'num_end'],
        col_upd=['capacity', 'opsos', 'region', 'territory', 'inn'],
        col_names=['num_prefix', 'num_start', 'num_end', 'capacity', 'opsos', 'region', 'territory', 'inn'],
    )
