from rest_framework import serializers
from abcdef import models as abcdef_models


class PhoneSerializer(serializers.ModelSerializer):
    num_min = serializers.ReadOnlyField()
    num_max = serializers.ReadOnlyField()

    class Meta:
        model = abcdef_models.Phone
        fields = '__all__'


class TerritorySerializer(serializers.ModelSerializer):

    class Meta:
        model = abcdef_models.Territory
        fields = '__all__'


class OpsosSerializer(serializers.ModelSerializer):

    class Meta:
        model = abcdef_models.Opsos
        fields = '__all__'


class PhoneNormSerializer(serializers.ModelSerializer):
    opsos = OpsosSerializer()
    territory = TerritorySerializer()

    class Meta:
        model = abcdef_models.PhoneNorm
        fields = '__all__'
