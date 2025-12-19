from django.contrib import admin
from abcdef import models as abcdef_models


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['num_prefix', 'num_min', 'num_max', 'capacity', 'opsos', 'region', 'territory', 'inn']
    # list_display = ['num_prefix', 'num_start', 'num_end', 'capacity', 'opsos', 'region', 'territory', 'inn']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PhoneNormAdmin(PhoneAdmin):
    list_display = ['num_prefix', 'num_min', 'num_max', 'capacity', 'opsos', 'territory', 'inn']


admin.site.register(abcdef_models.DownloadInfo)
admin.site.register(abcdef_models.Territory)
admin.site.register(abcdef_models.Opsos)
admin.site.register(abcdef_models.Phone, PhoneAdmin)
admin.site.register(abcdef_models.PhoneNorm, PhoneNormAdmin)
