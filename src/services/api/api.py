from django.urls import include
from dmr.routing import Router, path

from services.api.mobile.endpoints import urlpatterns as mobile_patterns

api = Router(
    prefix="api/",
    urls=[
        path("mobile/", include(mobile_patterns)),
    ],
)
