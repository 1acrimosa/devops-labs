from django.urls import path

from apps.metrics.api import views

app_name = "apps.metrics"

urlpatterns = [
    path("", views.metrics, name="metrics"),
]
