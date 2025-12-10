from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError
# from abcdef import validators


# вариант 1
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


# вариант 2
class PhoneNorm(models.Model):
    num_prefix = models.CharField(_('Префикс'), max_length=5, db_index=True)
    num_min = models.BigIntegerField(_('Начиная с'))
    num_max = models.BigIntegerField(_('Заканчивая по'))
    capacity = models.PositiveIntegerField(_('Емкость'))
    inn = models.CharField(_('ИНН'), max_length=20)
    opsos = models.ForeignKey('abcdef.Opsos', on_delete=models.PROTECT, null=True, verbose_name=_('Оператор'))
    territory = models.ForeignKey('abcdef.Territory', on_delete=models.PROTECT, null=True, verbose_name=_('Территория ГАР'), blank=True)

    class Meta:
        verbose_name = _("Реестр нумерации (нормализованный)")
        verbose_name_plural = _("Реестр нумерации (нормализованный)")
        unique_together = ('num_min', 'num_max')  # для пакетной вствки


class Opsos(models.Model):
    name = models.CharField(_('Оператор'), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Оператор")
        verbose_name_plural = _("Операторы")

    def __str__(self):
        return self.name


class Territory(models.Model):
    name = models.TextField(_('Территория ГАР'), unique=True)

    class Meta:
        verbose_name = _("Территория ГАР")
        verbose_name_plural = _("Территории ГАР")

    def __str__(self):
        return self.name
