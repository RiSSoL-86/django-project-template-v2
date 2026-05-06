from http import HTTPStatus

from dmr import ResponseSpec

from services.api.auth import AuthBearer
from services.api.common.controllers import AuthenticatedController
from services.api.mobile.users.services.me import MeService
from services.api.mobile.users.shemas import UserResponse


class MeController(AuthenticatedController):
    auth = [AuthBearer()]
    responses = [
        ResponseSpec(
            UserResponse,
            status_code=HTTPStatus.OK,
        ),
    ]

    def get(self) -> UserResponse:
        service = MeService()
        result = service.execute(self.user)
        return UserResponse.model_validate(result)
