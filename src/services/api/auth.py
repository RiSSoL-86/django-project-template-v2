from typing import final, override

from asgiref.sync import sync_to_async
from django.core.exceptions import SuspiciousOperation
from dmr.openapi.objects import SecurityScheme
from dmr.security import AsyncAuth
from oauth2_provider.oauth2_backends import get_oauthlib_core


@final
class AuthBearer(AsyncAuth):
    @override
    @property
    def security_schemes(self) -> dict[str, SecurityScheme]:
        return {
            "BearerAuth": SecurityScheme(type="http", scheme="bearer"),
        }

    @override
    @property
    def security_requirement(self) -> dict[str, list[str]]:
        return {"BearerAuth": []}

    @override
    async def __call__(self, endpoint, controller):
        request = controller.request

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        oauthlib_core = get_oauthlib_core()

        try:
            valid, r = await sync_to_async(oauthlib_core.verify_request)(
                request, scopes=[]
            )
        except ValueError as error:
            if str(error) == "Invalid hex encoding in query string.":
                raise SuspiciousOperation(error)
            raise
        else:
            if valid:
                request.auth = (r.user, r.access_token)
                return self

        request.oauth2_error = getattr(r, "oauth2_error", {})
        return None
