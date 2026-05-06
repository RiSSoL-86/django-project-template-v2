from django.urls import include, path
from dmr.openapi import build_schema
from dmr.openapi.views import SwaggerView
from dmr.plugins.pydantic import PydanticSerializer
from dmr.routing import Router, build_404_handler, build_500_handler

from services.api.mobile import urls as mobile_urls

router = Router(
    prefix="",
    urls=[
        path(
            mobile_urls.router.prefix,
            include((mobile_urls.router.urls, "mobile"), namespace="mobile"),
        ),
    ],
)

schema = build_schema(router)

urlpatterns = [
    path("api/", include((router.urls, "api"), namespace="api")),
    path("docs/", SwaggerView.as_view(schema), name="docs"),
]

handler404 = build_404_handler(
    router.prefix,
    serializer=PydanticSerializer,
)

handler500 = build_500_handler(
    router.prefix,
    serializer=PydanticSerializer,
)
