from django.conf import settings
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title=gettext_lazy("API"),
        default_version="v1",
        description=gettext_lazy("Development"),
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="unawares15@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = "api_v1"
urlpatterns = [
    path("thumbnails/", include("apps.thumbnails.api.urls")),
    path("metrics/", include("apps.metrics.api.urls")),
]

if settings.SWAGGER:
    urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
        ),
        re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]
