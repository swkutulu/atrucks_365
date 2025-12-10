import logging
from core.celery import app
from celery import shared_task
from abcdef import helpers


logger = logging.getLogger('celery')


@shared_task(bind=True)
def download_files_task(self):
    logger.info(">> Download task started ...")
    retry = False
    for link, file_name, base_name in helpers.get_files():
        # скачиваем и обрабатываем только, те файлы которых нет
        if helpers.download_file(link, file_name, base_name):
            process_file_task.delay(file_name, base_name)
        else:
            retry = True
    if retry:
        logger.info(">> !Download task retry ...")
        download_files_task.delay()
    logger.info("<< Download task finished ...")


@app.task(bind=True)
def process_file_task(self, file_name, base_name):
    logger.info(">> Process task started ...")
    helpers.process_file(file_name, base_name)
    logger.info("<< Procxess task finished ...")
