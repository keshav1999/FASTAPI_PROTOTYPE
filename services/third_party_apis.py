import traceback

import requests
from common.log_data import ApplicationLogger as applog
from common.secret_manager import SecreteData
from fastapi.exceptions import HTTPException


def fresh_work_api(data):
    key = SecreteData()
    try:
        header = {
            "Content-Type": 'application/json',
            "Authorization": "Basic " + key.FRESHWORKS_AUTH_TOKEN,
        }
        url = key.FRESHWORKS_BASE_URL + "/contacts"
        per_adress = ''
        if data.get('permanentAddress') != '':
            per_adress = ' '.join(data.get('permanentAddress').values())
        payload = {
            "name": "{} {} ".format(data.get('firstName'), data.get('lastName')),
            "address": per_adress,
            "description": ' ',
            "email": data.get('email'),
            "mobile": data.get('phoneNumber'),
            "unique_external_id": data.get('userUuid')
        }
        response = requests.post(url, headers=header, json=payload)
        app_response = response.json()
        if 'errors' in app_response:
            app_response['code'] = 500
        else:
            app_response['code'] = 200
    except Exception as exp:
        applog.error("Exception occured in replace_cc_by_uuid: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail="some went wrong {}".format(exp))
    finally:
        return app_response


def fresh_work_api_update(data, fw_external_id, card_last_four_digits):
    key = SecreteData()
    try:
        header = {
            "Content-Type": 'application/json',
            "Authorization": "Basic " + key.FRESHWORKS_AUTH_TOKEN,
        }
        url = key.FRESHWORKS_BASE_URL + f"/contacts/{fw_external_id}"
        if data.get('isSsn') == True:
            isSsn = "Yes"
        else:
            isSsn = "No"
        custom_fields = {}

        custom_fields['application_status'] = str(data.get('applicationStatus'))
        custom_fields['last_4_digits_of_ssn'] = str(data.get('ssnLastFourDigits'))[-4:]
        custom_fields['does_user_have_an_ssn'] = isSsn
        custom_fields['last_4_digit_of_neu_card'] = str(card_last_four_digits)
        per_adress = ''
        if data.get('permanentAddress') != '':
            per_adress = ' '.join(data.get('permanentAddress').values())
        payload = {
            "name": "{} {} ".format(data.get('firstName'), data.get('lastName')),
            "address": per_adress,
            "description": ' ',
            "email": data.get('email'),
            "mobile": data.get('phoneNumber'),
            "custom_fields": custom_fields
        }
        response = requests.put(url, headers=header, json=payload)
        app_response = response.json()
        if 'errors' in app_response:
            app_response['code'] = 500
        else:
            app_response['code'] = 200
    except Exception as exp:
        applog.error("Exception occured in replace_cc_by_uuid: \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail="some went wrong {}".format(exp))
    finally:
        return app_response
