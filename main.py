import os
import sys
from logging.config import dictConfig

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseSettings

from routers.cards import cards_router
from common.secret_manager import SecreteData
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config'))
from config.custom_log  import log_config
from common.app_constants import AppConstants
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from common.messages import Messages
from common.utilities import delete_422_response
class Settings(BaseSettings):
    """
    Use this class for adding constants
    """
    app_name: str = "IVR APP"


settings = Settings()
dictConfig(log_config)

# env loading
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(env_file, override=True)

app = FastAPI(docs_url=os.getenv("swagger_url"), redoc_url=os.getenv("doc_url")
              # servers=[
              #     {"url": "http://0.0.0.0:5000", "description": "Staging environment"},
              # ],
              )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(exc.detail),
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()  # dublicattion coming
    actual_dict = {
        "code": AppConstants.CODE_INVALID_REQUEST,
        "message": Messages.INVALID_FORMAT,
    }
    new_list = []
    for dictionary in details:
        if dictionary not in new_list:
            new_list.append(dictionary)

    modified_list = []
    for values in new_list:
        new_dict = {
            "field": values['loc'][1],
            "message": "Invalid " + values['loc'][1]
        }
        modified_list.append(new_dict)
        actual_dict['errors'] = modified_list
    return JSONResponse(
        status_code=AppConstants.CODE_INVALID_REQUEST,
        content=jsonable_encoder(actual_dict),
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="IVR PROJECT (BACKEND APIS)",
        version="2.0",
        description="This apis is used to support IVR functionalities :",
        routes=app.routes,
    )
    delete_422 = delete_422_response(openapi_schema["paths"])
    openapi_schema["info"]["x-logo"] = {
        "url": "https://d2o3z47i1v96zk.cloudfront.net/images/email-template-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
app.include_router(cards_router)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# calling middleware
# JwtMiddleWareToken = JwtMiddleWare(logger=logging)
# app.add_middleware(BaseHTTPMiddleware, dispatch=JwtMiddleWareToken)
keys = SecreteData()
if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=int(keys.PORT))
    # uvicorn.run(app, host="0.0.0.0", port=5000)