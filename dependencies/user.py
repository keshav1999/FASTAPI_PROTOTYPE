import traceback

from fastapi import Request
from fastapi.responses import JSONResponse

from common.app_response import AppResponse
from common.log_data import ApplicationLogger as applog
from common.messages import Messages
from repository.schema import card_summary
from repository.user import check_uuid_exist_db
from fastapi import FastAPI, HTTPException

async def user_check_exist(request: Request, data: card_summary):
    """ This function used to check user exist in database"""
    app_response = AppResponse()
    try:
        app_response = check_uuid_exist_db(data.customer_id)
    except Exception as exp:
        applog.error("Exception occurred in jwt token validation: \n{0}".format(traceback.format_exc()))
        return JSONResponse(status_code=500, content={"code": 500, "message": Messages.EXCEPTION_JWT})
    finally:
        if app_response['code'] == 200:
            pass
        else:
            return JSONResponse(status_code=400, content={"code": 400, "message": Messages.USER_NOT_FOUND})

