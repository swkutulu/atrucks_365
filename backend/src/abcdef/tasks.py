import logging
from core.celery import app
from celery import shared_task
from abcdef import helpers


logger = logging.getLogger('celery')


@shared_task(bind=True)
def download_files_task(self, try_count=0):
    logger.info(">> Download task started ...")
    retry = False
    for link, file_name, base_name in helpers.get_files():
        # скачиваем только те файлы, которых нет в ФС
        if not helpers.download_file(link, file_name, base_name, try_count):
            retry = True
    if retry:
        logger.info(">> !Download task retry ...")
        download_files_task.delay(try_count + 1)
    else:
        for _, file_name, base_name in helpers.get_files(True):
            process_file_task.delay(file_name, base_name)
    logger.info("<< Download task finished ...")


@app.task(bind=True)
def process_file_task(self, file_name, base_name):
    logger.info(f">> Process file task {base_name} started ...")
    helpers.process_file(file_name, base_name)
    logger.info(f"<< Process file task {base_name} finished ...")
