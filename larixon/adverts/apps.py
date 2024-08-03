from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdvertsConfig(AppConfig):
    name = "larixon.adverts"
    verbose_name = _("Adverts")
    default_auto_field = "django.db.models.BigAutoField"
