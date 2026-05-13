from typing import TYPE_CHECKING, final

from services.api.mobile.users.exceptions import UserInactiveError

if TYPE_CHECKING:
    from apps.users.models import User


@final
class MeService:
    async def execute(self, user: "User") -> "User":
        if not user.is_active:
            raise UserInactiveError("User is blocked")
        return user
