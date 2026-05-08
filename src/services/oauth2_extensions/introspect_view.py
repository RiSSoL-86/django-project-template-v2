import json
from typing import final, override

from django.http import HttpResponse
from oauth2_provider.views.introspect import (
    IntrospectTokenView as BaseIntrospectTokenView,
)

from apps.common.services.http import apply_response_headers
from services.oauth2_extensions.schemas import IntrospectTokenResponse


@final
class IntrospectTokenView(BaseIntrospectTokenView):
    @override
    @staticmethod
    def get_token_response(token_value=None):
        original_response = BaseIntrospectTokenView.get_token_response(
            token_value
        )
        data = json.loads(original_response.content)

        response_data = IntrospectTokenResponse(**data)

        response = HttpResponse(
            content=response_data.model_dump_json(by_alias=True),
            status=original_response.status_code,
        )
        return apply_response_headers(response, original_response.headers)
