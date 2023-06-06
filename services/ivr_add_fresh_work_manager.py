# from __future__ import annotations
#
# import traceback
#
# from common.app_response import AppResponse
# from common.messages import Messages
# from fastapi.exceptions import HTTPException
# from repository.user import add_user
# from services.third_party_apis import fresh_work_api
#
# from common.log_data import ApplicationLogger as applog
#
#
# def add_fresh_work_manager(header, user_uuid):
#     """ manager function to perform logic operation
#        api name : add_fresh_work_contact
#        return json response
#      """
#     app_response = AppResponse()
#     try:
#         applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | get user profile")
#         get_usr_res = "Asd"
#         applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | get user profile completed")
#         if get_usr_res['code'] == 200:
#             data = {"user_id": get_usr_res.get('data').get('userUuid')}
#             applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | calling fresh work api to add user details")
#             fresh_w_response = fresh_work_api(get_usr_res['data'])
#             applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | executed add contact fresh work")
#             if fresh_w_response['code'] == 200:
#                 applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | contact added")
#                 data['fw_id'] = fresh_w_response.get('id')
#                 app_response = add_user(data)
#                 applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | calling Database to add contact")
#                 if app_response['code'] == 200:
#                     applog.info(f"ADD FRESH WORK CONTACT | {user_uuid} | manager function executed")
#                     app_response.set_response(200, {}, Messages.SUCCESS, True)
#                 else:
#                     applog.error(f"ADD FRESH WORK CONTACT | {user_uuid} | manager function failed")
#                     app_response.set_response(500, {}, Messages.FAILED, False)
#             else:
#                 applog.error(f"ADD FRESH WORK CONTACT | {user_uuid} | fresh work add contact failed")
#                 app_response.set_response(400, fresh_w_response['errors'], Messages.FRESH_WORK_ADD_FAILED, False)
#         else:
#             applog.error(f"ADD FRESH WORK CONTACT | {user_uuid} | Given user profile information not found")
#             app_response.set_response(400, {}, Messages.USER_INFO_FAILED, False)
#
#     except Exception as exp:
#         applog.error("Exception occurred in ADD CONTACT card: \n{0}".format(traceback.format_exc()))
#         raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.CARD_BLOCKED_FAILED})
#     finally:
#         return app_response
