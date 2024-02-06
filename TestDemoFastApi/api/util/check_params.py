from util.code import code
import re
from fastapi import Request
from common.mysql_common import db
from common.encryption import ep
from sqlalchemy import Column, Integer, String, ForeignKey,select
from api.Model.DBModel.user.Entity.userEntity import userEntity

#逻辑判断

def check_add_user_params(request: Request,params: dict):
    """
    检查登录参数
    :param params: 登录参数
    :return: 自定义的关键字返回结果
    """
    status = (
        {"code": code.REQUEST_MODE_ERROR, "msg": code.REQUEST_MODE_ERROR_MSG} if not request.method == 'POST'
        else
        {"code": code.USER_REQUEST_FORMAT_ERROR, "msg": code.USER_REQUEST_FORMAT_ERROR_MSG} if not request.headers['Content-Type'] == 'application/json'
        else
        {"code": code.USER_PARAMS_IS_NULL_ERROR, "msg": code.USER_PARAMS_IS_NULL_ERROR_MSG} if not all(value != "" for value in params.values())
        else
        {"code": code.USER_ACCOUNT_START8_END18_ERROR, "msg": code.USER_ACCOUNT_START8_END18_ERROR_MSG} if not 8 < len(params.get('u_account')) < 18
        else
        {"code": code.USER_PHONE_IS_NOT_11_ERROR, "msg": code.USER_PHONE_IS_NOT_11_ERROR_MSG} if not len(params.get('u_phone')) == 11
        else
        {"code": code.USER_PHONE_TYPE_INT_ERROR, "msg": code.USER_PHONE_TYPE_INT_ERROR_MSG} if not isinstance(int(params.get('u_phone')), int)
        else
        {"code": code.USER_PASSWORD_FORMAT_AND_LENGTH_ERROR,"msg": code.USER_PASSWORD_FORMAT_AND_LENGTH_ERROR_MSG} if re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,30}$').match(params.get('u_passwd')) is None
        else
        {"code": code.USER_USERNAME_LENGTH_ERROR, "msg": code.USER_USERNAME_LENGTH_ERROR_MSG} if not 1 < len(params.get('u_name')) < 10
        else
        {"code": code.USER_NAME_IS_CHINESE_ERROR, "msg": code.USER_NAME_IS_CHINESE_ERROR_MSG} if not re.compile(r'^[\u4e00-\u9fa5]+$').match(params.get('u_name'))
        else
        {"code": code.USER_SEX_IS_BOY_OR_GIRL_ERROR, "msg": code.USER_SEX_IS_BOY_OR_GIRL_ERROR_MSG} if not params.get('u_sex') == '男' or params.get('u_sex') == '女'
        else
        {"code": code.USER_ADDRESS_LENGTH_100_ERROR, "msg": code.USER_ADDRESS_LENGTH_100_ERROR_MSG} if not len(params.get('u_address')) < 100
        else
        True
        )

    return status


def check_login_request_params_is_null(request: Request,params: dict):
    """
    检查登录参数
    :param params: 登录参数
    :return: 自定义的关键字返回结果
    """
    status=(
        {"code": code.REQUEST_MODE_ERROR, "msg": code.REQUEST_MODE_ERROR_MSG} if not  request.method == 'POST'
        else
        {"code": code.USER_REQUEST_FORMAT_ERROR, "msg": code.USER_REQUEST_FORMAT_ERROR_MSG} if not request.headers['Content-Type'] == 'application/json'
        else
        {"code": code.USER_ACCOUNT_OR_PASSWORD_NOT_NULL_ERROR, "msg": code.USER_ACCOUNT_OR_PASSWORD_NOT_NULL_ERROR_MSG} if not  params['u_account'] and params['u_passwd']
        else
        True
    )
    return status

def check_login_request_account_and_token_is_not(params:dict,data:dict):

    status = (
        {"code": code.USER_ACCOUNT_IS_NO_ERROR, "msg": code.USER_ACCOUNT_IS_NO_ERROR_MSG} if not data
        else
        {"code": code.USER_ACCOUNT_IS_NO_ERROR, "msg": code.USER_ACCOUNT_IS_NO_ERROR_MSG} if  data[0][0] != ep(password=params['u_passwd']).md5()
        else
        True
    )
    return status