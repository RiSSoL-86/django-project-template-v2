from django.http import HttpResponse


def apply_response_headers(
    response: HttpResponse, headers: dict
) -> HttpResponse:
    """
    Applies headers from a dictionary to a Django HttpResponse.
    """
    for k, v in headers.items():
        response[k] = v
    return response
