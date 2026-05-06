from django.urls import include, path
from dmr.openapi import build_schema
from dmr.openapi.views import SwaggerView

from services.api.api import api

schema = build_schema(api)

urlpatterns = [
    path("", include(api.urls)),
    path("docs/", SwaggerView.as_view(schema)),
]
