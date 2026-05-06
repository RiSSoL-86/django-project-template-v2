from dmr.routing import Router, path

from services.api.mobile.users.endpoints import MeController

router = Router(
    prefix="users/",
    urls=[
        path("me", MeController.as_view(), name="me"),
    ],
)
