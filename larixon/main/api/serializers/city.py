from rest_framework import serializers

from larixon.main.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id"]


class CityListSerializer(CitySerializer):
    class Meta(CitySerializer.Meta):
        fields = CitySerializer.Meta.fields + ["name"]


class CityCreateSerializer(CitySerializer):
    class Meta(CitySerializer.Meta):
        fields = ["name"]
