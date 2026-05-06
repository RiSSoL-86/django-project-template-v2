from apps.users.models import User


class MeService:
    async def execute(self, user: User):
        return user
