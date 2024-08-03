from rest_framework import serializers

from larixon.adverts.models import Advert
from larixon.main.api.serializers.category import CategorySerializer
from larixon.main.api.serializers.city import CitySerializer
from larixon.users.api.serializers import UserSerializer


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ["id"]


class AdvertListSerializer(AdvertSerializer):
    class User(UserSerializer):
        class Meta(UserSerializer.Meta):
            fields = UserSerializer.Meta.fields + ["name"]

    class City(CitySerializer):
        class Meta(CitySerializer.Meta):
            fields = CitySerializer.Meta.fields + ["name"]

    class Category(CategorySerializer):
        class Meta(CategorySerializer.Meta):
            fields = CategorySerializer.Meta.fields + ["name"]

    user = User()
    city = City()
    category = Category()

    class Meta(AdvertSerializer.Meta):
        fields = ["id", "user", "city", "category", "num_views", "description"]


class AdvertCreateSerializer(AdvertSerializer):
    class Meta(AdvertSerializer.Meta):
        fields = ["title", "city", "category", "description"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data=validated_data)


class AdvertRetrieveSerializer(AdvertListSerializer):
    class Meta(AdvertListSerializer.Meta):
        ...
