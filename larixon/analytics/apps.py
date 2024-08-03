from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnalyticsConfig(AppConfig):
    name = "larixon.analytics"
    verbose_name = _("Analytics")
    default_auto_field = "django.db.models.BigAutoField"
