from django.db.models.functions import Random


class BaseQuerySetMixin:

    def random(self):
        q = self.annotate(_random=Random())
        return q.order_by("_random").first()


class AllObjectsManagerMixin:
    def get_queryset(self, request):
        qs = getattr(self.model, "all_objects").get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


class AvailableQuerySetMixin(BaseQuerySetMixin):

    def available(self):
        return self.filter(is_removed=False)
