from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from larixon.adverts.api.views import AdvertViewSet
from larixon.main.api.views import CityViewSet, CategoryViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("cities", CityViewSet, "city")
router.register("adverts", AdvertViewSet, "advert")
router.register("categories", CategoryViewSet, "category")

app_name = "api"
urlpatterns = router.urls
