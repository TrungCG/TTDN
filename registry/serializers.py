from rest_framework import serializers
from .models import (
    ProvinceOld, District, CommuneOld, 
    ProvinceNew, CommuneNew, CommuneHistory
)

class ProvinceOldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceOld
        fields = "__all__"

class DistrictSerializer(serializers.ModelSerializer):
    province = ProvinceOldSerializer(read_only=True)

    class Meta:
        model = District
        fields = "__all__"

class CommuneOldSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    province = ProvinceOldSerializer(read_only=True)

    class Meta:
        model = CommuneOld
        fields = "__all__"

class ProvinceNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceNew
        fields = "__all__"

class CommuneNewSerializer(serializers.ModelSerializer):
    province = ProvinceNewSerializer(read_only=True)

    class Meta:
        model = CommuneNew
        fields = "__all__"

class CommuneHistorySerializer(serializers.ModelSerializer):
    commune_old = CommuneOldSerializer(read_only=True)
    commune_new = CommuneNewSerializer(read_only=True)

    class Meta:
        model = CommuneHistory
        fields = "__all__"

# class ProvinceHistorySerializer(serializers.ModelSerializer):
#     province_old = ProvinceOldSerializer(read_only=True)
#     province_new = ProvinceNewSerializer(read_only=True)

#     class Meta:
#         model = ProvinceHistory
#         fields = "__all__"
