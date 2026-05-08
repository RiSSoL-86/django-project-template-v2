import datetime
from typing import Optional

from services.api.common.schemas import CamelCaseModel


class TokenUser(CamelCaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    last_login: Optional[datetime.datetime] = None
    date_joined: Optional[datetime.datetime] = None


class TokenResponse(CamelCaseModel):
    access_token: str
    expires_in: int
    token_type: str
    scope: str
    refresh_token: Optional[str] = None
    user: TokenUser


class IntrospectTokenResponse(CamelCaseModel):
    active: bool
    scope: Optional[str] = None
    exp: Optional[int] = None
    client_id: Optional[str] = None
    username: Optional[str] = None
