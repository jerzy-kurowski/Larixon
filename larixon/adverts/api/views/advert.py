from larixon.adverts.api.serializers.advert import AdvertSerializer, AdvertRetrieveSerializer, AdvertCreateSerializer, \
    AdvertListSerializer
from larixon.adverts.models import Advert
from larixon.analytics.tasks import create_advert_view
from larixon.utils.api.mixins import MultiFilterSetMixin, CustomCreateModelMixin, CustomRetrieveModelMixin, \
    MultiSerializerMixin, CustomListModelMixin
from larixon.utils.api.viewsets import CustomGenericViewSet


class AdvertViewSet(
    MultiFilterSetMixin,
    MultiSerializerMixin,
    CustomListModelMixin,
    CustomCreateModelMixin,
    CustomRetrieveModelMixin,
    CustomGenericViewSet,
):
    serializer_action_classes = {
        "_": AdvertSerializer,
        "list": AdvertListSerializer,
        "create": AdvertCreateSerializer,
        "retrieve": AdvertRetrieveSerializer,
    }

    def get_queryset(self):
        return Advert.objects.select_related("user", "city", "category")

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        create_advert_view.delay(kwargs["pk"], self.request.META["REMOTE_ADDR"])
        return response
