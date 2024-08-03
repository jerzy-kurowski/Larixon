from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from .mixins import (
    MultiSerializerMixin,
    CustomPartialUpdateModelMixin,
    CustomRetrieveModelMixin,
    CustomListModelMixin,
    CustomCreateModelMixin,
)


class CustomGenericViewSet(GenericViewSet):
    def get_serializer(self, *args, **kwargs) -> Serializer:
        return super().get_serializer(*args, **kwargs)


class CustomViewSet(
    MultiSerializerMixin,
    CustomListModelMixin,
    CustomCreateModelMixin,
    CustomRetrieveModelMixin,
    CustomPartialUpdateModelMixin,
    CustomGenericViewSet,
):
    ...
