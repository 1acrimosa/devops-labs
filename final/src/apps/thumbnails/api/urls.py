from django.urls import re_path

from apps.thumbnails.api import views

app_name = "apps.thumbnails"

urlpatterns = [
    re_path(
        r"^(?P<max_height>\d+)x(?P<max_width>\d+)/(?P<url>.+)/$", views.resize, name="thumbnail"
    ),
]
