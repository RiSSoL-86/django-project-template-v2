import hashlib
import json
from typing import final, override

from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from oauth2_provider.views.base import TokenView as BaseTokenView

from apps.common.services.http import apply_response_headers
from services.oauth2_extensions.schemas import TokenResponse, TokenUser


@final
class TokenView(BaseTokenView):
    @override
    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            parsed_body = json.loads(body)
            access_token = parsed_body.get("access_token")

            if access_token is not None:
                token_checksum = hashlib.sha256(
                    access_token.encode("utf-8")
                ).hexdigest()
                token = (
                    get_access_token_model()
                    .objects.select_related("user")
                    .get(token_checksum=token_checksum)
                )
                app_authorized.send(sender=self, request=request, token=token)

                # customize response
                response_data = TokenResponse(
                    access_token=parsed_body["access_token"],
                    expires_in=parsed_body["expires_in"],
                    token_type=parsed_body["token_type"],
                    scope=parsed_body["scope"],
                    refresh_token=parsed_body.get("refresh_token"),
                    user=TokenUser.model_validate(token.user),
                )

                body = response_data.model_dump_json(by_alias=True)

        response = HttpResponse(content=body, status=status)
        return apply_response_headers(response, headers)
