from django.conf import settings
from django.db import models
from django.db.models.functions import Concat, Cast
# from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import AllowAny
from abcdef import models as abcdef_models
from abcdef import serializers as abcdef_serializers


class PhoneSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        qs = abcdef_models.Phone.objects.all()
        # qs = qs.annotate(
        #     num_min=Cast(Concat(models.F('num_prefix'), models.F('num_start')), output_field=models.BigIntegerField()),
        #     num_max=Cast(Concat(models.F('num_prefix'), models.F('num_end')), output_field=models.BigIntegerField()),
        # )
        phone = int(kwargs.get('phone'))
        if phone:
            qs = qs.filter(num_min__lte=phone, num_max__gte=phone)
        res = abcdef_serializers.PhoneSerializer(qs[:settings.PAGE_SIZE], many=True).data
        return Response(res)


class PhoneNormSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        qs = abcdef_models.PhoneNorm.objects.all().select_related('opsos', 'territory')
        phone = kwargs.get('phone')
        if len(phone) == 11:
            phone = phone[1:]
        prefix = phone[:3]
        if phone:
            phone = int(phone)
            qs = qs.filter(num_prefix=prefix, num_min__lte=phone, num_max__gte=phone)
        if qs.count():
            print(qs.query)
            res = abcdef_serializers.PhoneNormSerializer(qs[:settings.PAGE_SIZE], many=True).data
            return Response(res)
        return Response({'message': 'Телефон не найден'}, HTTP_404_NOT_FOUND)
