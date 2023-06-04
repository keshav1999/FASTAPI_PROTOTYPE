from __future__ import annotations

from functools import lru_cache

from common.app_response import AppResponse
from common.messages import Messages
from fastapi.exceptions import HTTPException
from repository.database import Session, engine
from sqlalchemy import MetaData, Table
from sqlalchemy import insert


@lru_cache()
def get_db():
    return Session()


@lru_cache()
def get_fresh_work_table():
    return Table("user_freshworks_mapping", MetaData(), autoload_with=engine)


session = get_db()
fresh_work_mapping = get_fresh_work_table()


def check_uuid_exist_db(id):
    """ this function execute for fetching the user exist in database"""
    try:
        app_response = AppResponse()
        item = session.query(fresh_work_mapping).filter(fresh_work_mapping.c.user_uuid == str(id)).first()
        if item:
            app_response.set_response(200, {"fw_external_id": item.fw_external_id}, "customer id found ", True)
        else:
            app_response.set_response(500, {}, "customer not found ", True)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.SOMETHING_WENT_WRONG})
    finally:
        return app_response


def add_user(data):
    try:
        app_response = AppResponse()
        stmt = (
            insert(fresh_work_mapping).
            values(user_uuid=data.get('user_id'), fw_external_id=data.get('fw_id'))
        )
        session.execute(stmt)
        session.commit()
        app_response.set_response(200, {}, "Data updation success", True)
    except Exception as exp:
        app_response.set_response(500, {}, "Data updation Failed", False)
        raise HTTPException(status_code=500, detail=Messages.HEADER_CONTAINS)
    finally:
        return app_response
