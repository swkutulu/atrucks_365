from django.db import models
from django.utils.translation import gettext_lazy as _


class DownloadInfo(models.Model):
    name = models.CharField(_('Название'), max_length=255, unique=True)
    link = models.URLField(_('Ссылка'))
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    is_downloaded = models.BooleanField(_('Скачан'), default=False)
    is_added = models.BooleanField(_('Добавлен'), default=False)
    retry_count = models.PositiveIntegerField(_('Попыток'), default=0)
    status_message = models.TextField(_('Статус'), null=True, blank=True)

    class Meta:
        verbose_name = _("Скачанный файл")
        verbose_name_plural = _("Скачанные файлы")

    def __str__(self):
        return self.name
