from django.urls import include
from dmr.routing import Router, path

from services.api.mobile.users import urls as users_urls

router = Router(
    prefix="mobile/",
    urls=[
        path(
            users_urls.router.prefix,
            include((users_urls.router.urls, "users"), namespace="users"),
        ),
    ],
)
