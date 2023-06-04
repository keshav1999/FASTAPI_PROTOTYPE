from uuid import UUID

from common.messages import Messages
from pydantic import BaseModel


class card_summary(BaseModel):
    customer_id: UUID
    mobile: str
    email: str


responses = {
    400: {"description": "Validation Error",
          "content": {
              "application/json": {
                  "example": {"code": 401, "message": Messages.INVALID_FORMAT, "errors": []}
              }}},
    401: {"description": "Authorization token is Invalid",
          "content": {
              "application/json": {
                  "example": {"code": 401, "message": Messages.AUTHORIZATION_FAILED}
              }}},
    500: {"description": "Internal Server Error",
          "content": {
              "application/json": {
                  "example": {"code": 500, "message": Messages.SOMETHING_WENT_WRONG}
              }}},
}
