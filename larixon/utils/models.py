from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from model_utils.models import SoftDeletableModel as BaseSoftDeletableModel


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``modified_at`` fields.

    """

    created_at = AutoCreatedField(_("Created At"), db_index=True)
    modified_at = AutoLastModifiedField(_("Modified At"), db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified_at field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get("update_fields", None)
        if update_fields:
            kwargs["update_fields"] = set(update_fields).union({"modified_at"})

        super().save(*args, **kwargs)


class SoftDeletableModel(BaseSoftDeletableModel):
    is_removed = models.BooleanField(_("Is Removed"), default=False)

    class Meta(BaseSoftDeletableModel.Meta):
        abstract = True



