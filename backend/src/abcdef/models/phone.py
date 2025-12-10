from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError
# from abcdef import validators


# АВС/ DEF;От;До;Емкость;Оператор;Регион;Территория ГАР;ИНН
class Phone(models.Model):
    num_prefix = models.CharField(_('Префикс'), max_length=5)
    num_start = models.CharField(_('Начиная с'), max_length=20)
    num_end = models.CharField(_('Заканчивая по'), max_length=20)
    capacity = models.PositiveIntegerField(_('Емкость'))
    opsos = models.CharField(_('Оператор'), max_length=255)
    region = models.CharField(_('Регион'), max_length=500)
    territory = models.TextField(_('Территория ГАР'), null=True, blank=True)
    inn = models.CharField(_('ИНН'), max_length=20)

    class Meta:
        verbose_name = _("Реестр нумерации")
        verbose_name_plural = _("Реестр нумерации")
        unique_together = ('num_prefix', 'num_start', 'num_end')
