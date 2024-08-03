from django.db.models import ForeignKey, GenericIPAddressField, CASCADE
from django.utils.translation import gettext_lazy as _

from larixon.utils.models import TimeStampedModel, SoftDeletableModel


class AdvertView(TimeStampedModel, SoftDeletableModel):
    advert = ForeignKey(
        "adverts.Advert",
        on_delete=CASCADE,
        verbose_name=_("Advert"),
    )
    ip_address = GenericIPAddressField(
        _("IP Address"),
        db_index=True,
    )

    class Meta:
        verbose_name = _("Advert View")
        verbose_name_plural = _("Advert Views")
