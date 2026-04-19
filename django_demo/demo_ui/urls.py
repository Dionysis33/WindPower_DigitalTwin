from django.urls import path

from .views import artifacts_view, home_view, parks_view, scope_view

urlpatterns = [
    path("", home_view, name="home"),
    path("parks/", parks_view, name="parks"),
    path("artifacts/", artifacts_view, name="artifacts"),
    path("scope/", scope_view, name="scope"),
]