from rest_framework import serializers

from larixon.main.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id"]


class CategoryListSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ["name"]


class CategoryCreateSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = ["name"]
