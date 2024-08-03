from django.urls import path

from .views import (
    user_detail_view,
    user_update_view,
    user_redirect_view,
)

app_name = "users"
urlpatterns = [
path("~update/", view=user_update_view, name="update"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
