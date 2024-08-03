from larixon.utils.api.mixins import CustomCreateModelMixin, CustomListModelMixin, MultiSerializerMixin
from larixon.utils.api.viewsets import CustomGenericViewSet
from ..serializers.city import CityListSerializer, CityCreateSerializer
from ...models import City


class CityViewSet(
    MultiSerializerMixin,
    CustomCreateModelMixin,
    CustomListModelMixin,
    CustomGenericViewSet
):
    serializer_action_classes = {
        "list": CityListSerializer,
        "create": CityCreateSerializer,
    }

    def get_queryset(self):
        return City.available_objects.all()
