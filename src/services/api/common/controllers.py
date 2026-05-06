from typing import cast

from dmr import Controller
from dmr.plugins.pydantic import PydanticSerializer
from oauth2_provider.models import AccessToken

from apps.users.models import User


class AuthenticatedController(Controller[PydanticSerializer]):
    @property
    def _auth_data(self) -> tuple[User, AccessToken]:
        """Helper property for retrieving authorization data."""
        auth = getattr(self.request, "auth", None)
        if auth is None:
            raise AttributeError(
                f"Controller '{self.__class__.__name__}' requires authentication. "
                "Make sure you have added 'auth = [AuthBearer()]' to the controller."
            )
        return cast(tuple[User, AccessToken], auth)

    @property
    def user(self) -> User:
        return self._auth_data[0]

    @property
    def token(self) -> AccessToken:
        return self._auth_data[1]
