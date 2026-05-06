from http import HTTPStatus

from dmr import Controller, ResponseSpec
from dmr.plugins.pydantic import PydanticSerializer

from services.api.auth import AuthBearer
from services.api.mobile.users.services.me import MeService
from services.api.mobile.users.shemas import UserResponse


class MeController(Controller[PydanticSerializer]):
    auth = [AuthBearer()]
    responses = [
        ResponseSpec(
            UserResponse,
            status_code=HTTPStatus.OK,
        ),
    ]

    def get(self, request) -> UserResponse:
        user, _ = request.auth

        service = MeService()
        result = service.execute(user)
        return result
