import traceback

import jwt
from common.app_response import AppResponse
from common.log_data import ApplicationLogger as applog
from common.messages import Messages
from common.secret_manager import SecreteData
from fastapi import HTTPException
from fastapi import Request, Header


async def jwt_validation_internal(request: Request):
    """ This function used to validate the jwt token"""
    applog.info(f"JWT VALIDATION INTERNAL TOKEN | requesting headers ")
    headers = request.headers
    applog.info(f"JWT VALIDATION INTERNAL TOKEN | Successfully received headers {headers} ")
    keys = SecreteData()
    app_response = AppResponse()
    key = keys.FRESHWORKS_IVR_JWT_SECRET
    token = None
    if 'Authorization' in headers:
        bearer = headers.get('Authorization')
        if 'Bearer' in bearer:
            token = bearer.split()[1]
        else:
            raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
    if not token:
        raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_MISSING})
    try:
        data = jwt.decode(token, key, algorithms=["HS256"])
        app_response.set_response(200, {}, "jwt token validation success", True)
    except jwt.ExpiredSignatureError as exp:
        raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
    except Exception as exp:
        applog.error("Exception occurred in jwt token validation internal: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_FAILED})


async def jwt_validation_external_validation(request: Request):
    """ This function used to validate the jwt token"""
    applog.info(f"JWT VALIDATION EXTERNAL TOKEN | requesting headers ")
    headers = request.headers
    applog.info(f"JWT VALIDATION EXTERNAL TOKEN | Successfully received headers {headers}")
    keys = SecreteData()
    applog.info("Ending Secreat manager")
    app_response = AppResponse()
    key = keys.FRESHWORKS_EXTERNAL_JWT_SECRET
    token = None
    if 'Authorization' in headers:
        bearer = headers.get('Authorization')
        if 'Bearer' in bearer:
            token = bearer.split()[1]
        else:
            raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
    if not token:
        raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_MISSING})
    try:
        data = jwt.decode(token, key, algorithms=["HS256"])
        app_response.set_response(200, {}, "jwt token validation success", True)
    except jwt.ExpiredSignatureError as exp:
        raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
    except Exception as exp:
        applog.error("Exception occurred in jwt token validation external: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=401, detail={"code": 401, "message": Messages.AUTHORIZATION_FAILED})
