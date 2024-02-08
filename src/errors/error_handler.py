from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessable


def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessable):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
