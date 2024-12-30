from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

api = [
    path("v1/", include("common.urls.v1", namespace="v1")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api)),
    path("healthcheck/", include("health_check.urls")),
]

if settings.LOCAL_SERVE_MEDIA:
    urlpatterns += static("media/", document_root=settings.MEDIA_ROOT)

if settings.LOCAL_SERVE_STATIC:
    urlpatterns += static("static/", document_root=settings.STATIC_ROOT)
