from larixon.utils.api.mixins import CustomCreateModelMixin, CustomListModelMixin, MultiSerializerMixin
from larixon.utils.api.viewsets import CustomGenericViewSet
from ..serializers.category import CategoryListSerializer, CategoryCreateSerializer
from ...models import Category


class CategoryViewSet(
    MultiSerializerMixin,
    CustomCreateModelMixin,
    CustomListModelMixin,
    CustomGenericViewSet
):
    serializer_action_classes = {
        "list": CategoryListSerializer,
        "create": CategoryCreateSerializer,
    }

    def get_queryset(self):
        return Category.available_objects.all()
