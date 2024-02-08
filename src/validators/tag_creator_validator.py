from cerberus import Validator
from src.erros.error_type.http_unprocessable_entity import HttpUnprocessableEntityError

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code": { "type": "string", "required": True, "empty": False }
    })

    response = body_validator.validate(request.jason)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
