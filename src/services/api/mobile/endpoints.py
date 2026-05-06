from dmr.routing import path

from services.api.mobile.users.endpoints import MeController

urlpatterns = [
    path("users/me", MeController.as_view(), name="me"),
]
