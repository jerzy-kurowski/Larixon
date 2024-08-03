from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    name = "larixon.main"
    verbose_name = _("Main")
    default_auto_field = "django.db.models.BigAutoField"
