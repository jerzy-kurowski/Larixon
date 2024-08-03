from django.db.models import Model
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from larixon.utils.api.serializers.responses import UUIDResponseSerializer


class MultiFilterSetMixin:
    filterset_action_classes: dict

    @property
    def filterset_class(self):
        return self.get_filterset_class()

    def get_filterset_class(self):
        if self.filterset_action_classes:
            try:
                return self.filterset_action_classes[self.action]
            except (KeyError, AttributeError):
                pass


class MultiSerializerMixin:
    serializer_action_classes: dict

    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        """
        if self.serializer_action_classes:
            try:
                return self.serializer_action_classes[self.action]
            except (KeyError, AttributeError):
                if self.serializer_action_classes.get("_"):
                    return self.serializer_action_classes["_"]
                elif self.serializer_action_classes.get("update_partial"):
                    return self.serializer_action_classes["update_partial"]

        return super().get_serializer_class()


class BaseCustomUpdateModelMixin:
    """
    Update a model instance.
    """

    def _update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer) -> Model:
        obj = serializer.save()
        return self.perform_post_update(obj)

    def perform_post_update(self, obj: Model) -> Model:
        return obj


class CustomListModelMixin(ListModelMixin):
    ...


class CustomCreateModelMixin(CreateModelMixin):
    """
    Create a model instance, perform post create action and return model id
    """

    def perform_post_create(self, obj: Model) -> Model:
        return obj

    def perform_create(self, serializer) -> Model:
        obj = serializer.save()
        return self.perform_post_create(obj)

    @extend_schema(
        responses={201: UUIDResponseSerializer()},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        return Response({"id": obj.pk}, status=status.HTTP_201_CREATED)


class CustomRetrieveModelMixin(RetrieveModelMixin):
    ...


class CustomUpdateModelMixin(BaseCustomUpdateModelMixin):
    def update(self, request, *args, **kwargs):
        return super()._update(request, *args, **kwargs)


class CustomPartialUpdateModelMixin(BaseCustomUpdateModelMixin):
    @extend_schema(
        responses={
            204: None,
        },
    )
    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self._update(request, *args, **kwargs)
