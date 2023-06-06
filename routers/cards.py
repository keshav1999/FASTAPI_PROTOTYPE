from __future__ import annotations

import traceback
from uuid import UUID

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

auth_scheme = HTTPBearer()
from common.log_data import ApplicationLogger as applog
from common.messages import Messages
from dependencies.header_validation import jwt_validation_external_validation as jw_val_ext
from dependencies.header_validation import jwt_validation_internal as jw_val_int
from fastapi import APIRouter, Request, Depends
from fastapi import Header
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from repository.schema import card_summary, responses
# from services.ivr_add_fresh_work_manager import add_fresh_work_manager
# from services.ivr_mini_statement_manager import mini_statement_manager


cards_router = APIRouter(
    prefix='/cards'
)


@cards_router.post('/getIVRMiniStatement', dependencies=[Depends(jw_val_ext)],
                   response_model=card_summary, tags=["IVR"],
                   responses={**responses, 200: {"description": "Successful Response",
                "content": {
                "application/json": {
               "example": {"code": 200, "message": "OK", "data": {}}
                     }}}}, )
async def ivr_mini_statement_list(request: Request, data: card_summary,
                                  token: HTTPAuthorizationCredentials = Depends(auth_scheme),
                                  Content_Type: str = Header(default=None),
                                  X_Api_Key: str = Header(default=None)):
    """ get ivr mini statement function
        Args: Input Parameter
            Bearer Token
        Returns:
            Response JSON
        """
    try:
        applog.info(f" IVR MINI STATEMENT | {data.customer_id} | Starting the API call")
        header = request.headers
        applog.info(f" IVR MINI STATEMENT | {data.customer_id} | Calling Manager function")
        mini_statement_app_response = ""
        applog.info(f" IVR MINI STATEMENT | {data.customer_id} | Manager Function executed successfully ")
        if mini_statement_app_response['code'] == 200:
            applog.info(f" IVR MINI STATEMENT | {data.customer_id} | Api executed successfully with 200 status code ")
            return JSONResponse(status_code=200,
                                content={"code": 200, "message": "OK", "data": mini_statement_app_response['data']})
        else:
            applog.error(f" IVR MINI STATEMENT | {data.customer_id} | Api execution failed with 500 status code ")
            return JSONResponse(status_code=mini_statement_app_response['code'],
                                content={"code": mini_statement_app_response['code'],
                                         "message": mini_statement_app_response['message']})
    except Exception as exp:
        applog.error("Exception occured in ivrministatementlist: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.SOMETHING_WENT_WRONG})
    finally:
        pass



@cards_router.get('/add-fw-contact', dependencies=[Depends(jw_val_int)], tags=["IVR"],
                  responses={**responses, 200: {"description": "Successful Response",
                "content": {
                "application/json": {
                "example": {"code": 200, "message": Messages.SUCCESS} }}}},)
async def add_fresh_work_contact(request: Request, user_uuid: UUID,
    Authorization: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    """ get add fresh work contact
        Args: Input Parameter
            Bearer Token
        Returns:
            Response JSON
        """
    try:
        applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | Starting the API call")
        header = request.headers
        applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | Starting the manager function")
        add_fresh_response = ""
        applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} |  manager function executed ")
        if add_fresh_response['code'] == 200:
            applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | API executed ")
            return JSONResponse(status_code=200, content={"code": 200, "message": Messages.SUCCESS})
        else:
            applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | API executed failed")
            return JSONResponse(status_code=add_fresh_response['code'],
                                content={"code": add_fresh_response['code'], "errors": add_fresh_response['data'],
                                         "message": add_fresh_response['message']})
    except Exception as exp:
        applog.error("Exception occurred in add fresh work contact: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.SOMETHING_WENT_WRONG})
    finally:
        pass


