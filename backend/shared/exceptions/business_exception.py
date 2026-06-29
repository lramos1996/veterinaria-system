from rest_framework.exceptions import (
    APIException
)


class BusinessException(
    APIException
):

    status_code = 400

    default_code = (
        "business_error"
    )

    default_detail = (
        "Error de negocio"
    )