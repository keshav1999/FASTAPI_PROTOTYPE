# from __future__ import annotations
#
# import traceback
#
# from common.app_response import AppResponse
# from common.log_data import ApplicationLogger as applog
# from common.messages import Messages
# from fastapi.exceptions import HTTPException
# from repository.database import Session, engine
# from services.internal_apis import get_user_details, ivr_ministatement_api
#
# session = Session(bind=engine)
#
#
# def mini_statement_manager(header, data):
#     """ manager function to perform logic operation
#        api name : get ivr mini statement
#        return json response with status code
#      """
#     app_response = AppResponse()
#     try:
#         applog.info(f" IVR MINI STATEMENT | {data.customer_id} | Getting user profile details by calling "
#                     f"get-user-profile API")
#         get_usr_res = get_user_details(header, data.customer_id)
#         if get_usr_res['code'] == 200:
#             applog.info(
#                 f" IVR MINI STATEMENT | {data.customer_id} | Got user profile details by calling get-user-profile API")
#             mail = get_usr_res['data']['email']
#             phone = get_usr_res['data']['phoneNumber']
#             if mail == data.email and phone == data.mobile:
#                 applog.info(
#                     f" IVR MINI STATEMENT | {data.customer_id} | Checking email and phone number with requested data")
#                 ivr_mini_resp = ivr_ministatement_api(data.customer_id, header)
#                 if ivr_mini_resp['code'] == 200:
#                     applog.info(
#                         f" IVR MINI STATEMENT | {data.customer_id} | Got mini statement by calling transaction list API")
#                     app_response.set_response(200, {"transactions": ivr_mini_resp['data']},
#                                               Messages.FETCH_MINI_STATEMENT_SUCCESS, True)
#                 else:
#                     applog.error(
#                         f" IVR MINI STATEMENT | {data.customer_id} | Failed to get mini statement from transaction list API")
#                     app_response.set_response(ivr_mini_resp['code'], {}, ivr_mini_resp['message'], False)
#             else:
#                 applog.error(
#                     f" IVR MINI STATEMENT | {data.customer_id} | Checking email and phone number failed")
#                 app_response.set_response(400, {}, Messages.USER_NOT_MOB_EMAIL, False)
#         else:
#             applog.error(
#                 f" IVR MINI STATEMENT | {data.customer_id} | User profile calling failed with status code 500")
#             app_response.set_response(400, {}, Messages.USER_INFO_FAILED, False)
#     except Exception as exp:
#         applog.error("Exception occured in ministatement_manager: \n{0}".format(traceback.format_exc()))
#         raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FETCH_MINI_STATEMENT_FAIL})
#     finally:
#         return app_response
