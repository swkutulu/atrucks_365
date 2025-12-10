from rest_framework import serializers
from abcdef import models as abcdef_models


class DownloadInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = abcdef_models.DownloadInfo
        fields = '__all__'
