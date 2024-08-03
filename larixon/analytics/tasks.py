from celery import shared_task
from django.db import transaction
from django.db.models import F

from larixon.adverts.models import Advert
from larixon.analytics.models import AdvertView


@shared_task()
def create_advert_view(
    advert_id: int,
    ip_address: str
):
    with transaction.atomic():
        _, is_created = AdvertView.objects.get_or_create(
            advert_id=advert_id, ip_address=ip_address,
        )
        if is_created:
            Advert.objects.filter(id=advert_id).update(
                num_views=F("num_views") + 1
            )
