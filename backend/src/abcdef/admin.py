from django.contrib import admin
import abcdef.models as abcdef_models


# class PhoneAdmin(admin.ModelAdmin):
#     list_display = ['num_prefix',]


admin.site.register(abcdef_models.DownloadInfo)
admin.site.register(abcdef_models.Phone)
# admin.site.register(abcdef_models.Phone, abcdef_models.PhoneAdmin)
