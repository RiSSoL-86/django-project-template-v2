from services.api.common.schemas import CamelCaseModel


class UserResponse(CamelCaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool

    class Config:
        from_attributes = True
