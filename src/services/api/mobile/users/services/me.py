from typing import final

from apps.users.models import User
from services.api.mobile.users.exceptions import UserInactiveError


@final
class MeService:
    async def execute(self, user: User):
        if not user.is_active:
            raise UserInactiveError("User is blocked")
        return user
