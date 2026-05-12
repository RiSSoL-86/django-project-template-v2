from http import HTTPStatus
from typing import TYPE_CHECKING, Any, final, override

from django.http import HttpResponse
from dmr import ResponseSpec
from dmr.endpoint import Endpoint

from services.api.auth import AuthBearer
from services.api.common.controllers import AuthenticatedController
from services.api.mobile.users.exceptions import UserInactiveError
from services.api.mobile.users.schemas import UserResponse
from services.api.mobile.users.services.me import MeService

if TYPE_CHECKING:
    from dmr import Controller


@final
class MeController(AuthenticatedController):
    auth = [AuthBearer()]
    responses = [
        ResponseSpec(
            UserResponse,
            status_code=HTTPStatus.OK,
        ),
    ]

    async def get(self) -> UserResponse:
        service = MeService()
        result = await service.execute(self.user)
        return UserResponse.model_validate(result)

    @override
    async def handle_async_error(
        self,
        endpoint: Endpoint,
        controller: "Controller[Any]",
        exc: Exception,
    ) -> HttpResponse:
        """Handle custom errors for this controller."""
        if isinstance(exc, UserInactiveError):
            return self.to_error(str(exc), status_code=HTTPStatus.FORBIDDEN)
        return await super().handle_async_error(endpoint, controller, exc)
