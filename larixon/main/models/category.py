from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from larixon.utils.models import TimeStampedModel, SoftDeletableModel


class Category(TimeStampedModel, SoftDeletableModel):
    name = CharField(
        _("Name"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self) -> str:
        return self.name
