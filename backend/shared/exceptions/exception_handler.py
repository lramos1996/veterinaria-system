from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from shared.exceptions.business_exception import (
    BusinessException
)


def custom_exception_handler(exc, context):

    if isinstance(exc, BusinessException):

        return Response(
            {
                "error": str(exc)
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return exception_handler(
        exc,
        context
    )