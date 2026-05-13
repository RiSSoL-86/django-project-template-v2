from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from django.http import HttpResponse


def apply_response_headers(
    response: "HttpResponse", headers: dict[str, Any]
) -> "HttpResponse":
    """
    Applies headers from a dictionary to a Django HttpResponse.
    """
    for k, v in headers.items():
        response[k] = v
    return response
