from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from abcdef import models as abcdef_models
from abcdef import serializers as abcdef_serializers


class DownloadInfoModelViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = abcdef_models.DownloadInfo.objects.all()
    serializer_class = abcdef_serializers.DownloadInfoSerializer
    permission_classes = [IsAuthenticated]
