from django.db import models
from django.db.models import CharField, TextField, ForeignKey, BigIntegerField
from django.utils.translation import gettext_lazy as _

from larixon.utils.models import TimeStampedModel, SoftDeletableModel


class Advert(TimeStampedModel, SoftDeletableModel):
    title = CharField(
        _("Title"),
        max_length=255,
    )
    user = ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    city = ForeignKey(
        "main.City",
        on_delete=models.CASCADE,
        verbose_name=_("City"),
    )
    category = ForeignKey(
        "main.Category",
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
    )
    num_views = BigIntegerField(
        _("Views"),
        default=0,
    )
    description = TextField(
        _("Description"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Advert")
        verbose_name_plural = _("Advert")

    def __str__(self) -> str:
        return self.title
