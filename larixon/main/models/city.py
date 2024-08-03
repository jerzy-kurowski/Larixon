from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from larixon.utils.models import TimeStampedModel, SoftDeletableModel


class City(TimeStampedModel, SoftDeletableModel):
    name = CharField(
        _("Name"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self) -> str:
        return self.name
