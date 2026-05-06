from django.core.exceptions import SuspiciousOperation
from dmr.openapi.objects import SecurityScheme
from dmr.security import SyncAuth
from oauth2_provider.oauth2_backends import get_oauthlib_core


class AuthBearer(SyncAuth):
    @property
    def security_schemes(self) -> dict[str, SecurityScheme]:
        return {
            "BearerAuth": SecurityScheme(type="http", scheme="bearer"),
        }

    @property
    def security_requirement(self) -> dict[str, list[str]]:
        return {"BearerAuth": []}

    def __call__(self, endpoint, controller):
        request = controller.request

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        oauthlib_core = get_oauthlib_core()

        try:
            valid, r = oauthlib_core.verify_request(request, scopes=[])
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
