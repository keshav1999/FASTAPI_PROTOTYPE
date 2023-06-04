import traceback
import requests
from common.app_response import AppResponse
from common.log_data import ApplicationLogger as applog
from common.messages import Messages
from common.secret_manager import SecreteData
from fastapi.exceptions import HTTPException


def get_user_details(headers, id):
    """ get user details function
            Args: Input Parameter
                Bearer Token
            Returns:
                Response JSON with status code and user profile details
            """
    response = AppResponse()
    keys = SecreteData()
    try:

        url = keys.INTERNAL_BASE_URL + "/identity/get-user-profile-by-uuid?user_uuid=" + str(id)
        headers = {
            "Content-Type": headers.get("Content-Type", 'application/json'),
            "Authorization": "Bearer " + keys.IDENTITY_JWT_TOKEN
        }
        response = requests.request("GET", url, headers=headers)
        response = response.json()
    except Exception as exp:
        applog.error("Exception occured in get user details: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail="some went wrong during user details fetching{}".format(exp))
    finally:
        return response


def ivr_ministatement_api(id, headers_data):
    """ get mini statement function
            Args: Input Parameter
                Bearer Token
            Returns:
                Response JSON
            """
    app_response = AppResponse()
    key = SecreteData()
    try:
        header = {
            "Content-Type": headers_data.get("Content-Type", 'application/json'),
            "Authorization": "Bearer " + key.CREDIT_CARD_JWT_TOKEN,
        }
        url = key.INTERNAL_BASE_URL + "/credit-card/get-transaction-list-by-uuid?user_uuid=" + str(id)
        response = requests.get(url, headers=header)
        app_response = response.json()
    except Exception as exp:
        applog.error("Exception occured in ivr mini statement : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.SOMETHING_WENT_WRONG})
    finally:
        return app_response


def get_account_summary(customer_id, headers_data):
    key = SecreteData()
    try:
        header = {
            "Content-Type": headers_data.get("Content-Type", 'application/json'),
            "Authorization": "Bearer " + key.CREDIT_CARD_JWT_TOKEN,
        }
        base_url_get_account = key.INTERNAL_BASE_URL + "/credit-card/get-cc-accounts-by-uuid"
        url = base_url_get_account + '/?user_uuid=' + str(customer_id)
        response = requests.get(url, headers=header)
        app_response = response.json()
    except Exception as exp:
        applog.error("Exception occured in get account summary: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail="something went wrong {}".format(exp))
    finally:
        return app_response


def replace_cc_by_uuid(id, headers_data):
    app_response = AppResponse()
    key = SecreteData()
    try:
        header = {
            "Content-Type": headers_data.get("Content-Type", 'application/json'),
            "Authorization": "Bearer " + key.CREDIT_CARD_JWT_TOKEN,
        }
        url = key.INTERNAL_BASE_URL + "/credit-card/replace-cc-by-uuid/" + f"?user_uuid={str(id)}&reissue_type={2}"
        response = requests.get(url, headers=header)
        app_response = response.json()
    except Exception as exp:
        applog.error("Exception occured in replace_cc_by_uuid: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.SOMETHING_WENT_WRONG})
    finally:
        return app_response


def   replace_cc_by_uuid_replace(id, headers_data):
    app_response = AppResponse()
    key = SecreteData()
    try:
        header = {
            "Content-Type": headers_data.get("Content-Type", 'application/json'),
            "Authorization": "Bearer " + key.CREDIT_CARD_JWT_TOKEN,
        }
        url = key.INTERNAL_BASE_URL + "/credit-card/replace-cc-by-uuid/" + f"?user_uuid={str(id)}&reissue_type={3}"
        response = requests.get(url, headers=header)
        app_response = response.json()
    except Exception as exp:
        applog.error("Exception occured in replace_cc_by_uuid: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.SOMETHING_WENT_WRONG})
    finally:
        return app_response
