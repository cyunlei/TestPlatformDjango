package com.msb.api.code;

/**
 * 系统管理模块的错误码
 * 区间：10000-15555
 */
public interface SystemCode {
    //系统通用的状态码
    String TRAFFIC_SYSTEM_SUCCESS = "000000";
    String TRAFFIC_SYSTEM_ERROR = "000001";
    /**
     * 错误 提示  警告
     */
    // 用户管理  10000-10999
    //10000-10499 错误的提示
    String SYSTEM_USER_ERROR_ADD_FAIL = "10000";
    //添加用户
    //用户参数为空
    String SYSTEM_USER_ERROR_ADD_FAIL_PARAM_NULL = "10001";
    String SYSTEM_USER_ERROR_ADD_FAIL_PARAM_NULL_msg = "用户参数为空";
    //用户名为空
    String SYSTEM_USER_ERROR_ADD_FAIL_NAME_NULL = "10002";
    String SYSTEM_USER_ERROR_ADD_FAIL_NAME_NULL_msg = "用户名为空";
    //账号为空
    String SYSTEM_USER_ERROR_ADD_FAIL_ACCOUNT_NULL = "10003";
    String SYSTEM_USER_ERROR_ADD_FAIL_ACCOUNT_NULL_msg = "账号为空";
    //密码为空
    String SYSTEM_USER_ERROR_ADD_FAIL_PASS_NULL = "10004";
    String SYSTEM_USER_ERROR_ADD_FAIL_PASS_NULL_msg = "密码为空";
    //手机为空
    String SYSTEM_USER_ERROR_ADD_FAIL_PHONE_NULL = "10005";
    String SYSTEM_USER_ERROR_ADD_FAIL_PHONE_NULL_msg = "手机为空";
    //用户名长度
    String SYSTEM_USER_ERROR_ADD_FAIL_NAME_SIZE = "10006";
    String SYSTEM_USER_ERROR_ADD_FAIL_NAME_SIZE_msg = "用户名长度小于3";
    //用户账号长度
    String SYSTEM_USER_ERROR_ADD_FAIL_ACCOUNT_SIZE = "10007";
    String SYSTEM_USER_ERROR_ADD_FAIL_ACCOUNT_SIZE_msg = "用户账号长度小于6";
    //用户密码长度
    String SYSTEM_USER_ERROR_ADD_FAIL_PASS_SIZE = "10008";
    String SYSTEM_USER_ERROR_ADD_FAIL_PASS_SIZE_msg = "用户密码长度小于6";
    //密码加密失败
    String SYSTEM_USER_ERROR_ADD_FAIL_PASS_ENCRYPTION_ERROR= "10009";
    String SYSTEM_USER_ERROR_ADD_FAIL_PASS_ENCRYPTION_ERROR_msg= "密码加密失败";


    //删除用户
    String SYSTEM_USER_ERROR_DEL_FAIL_UID_NULL= "10030";
    String SYSTEM_USER_ERROR_DEL_FAIL_UID_NULL_msg= "删除的用户uid为空";
    //删除失败
    //10500-10999 成功的提示
    int SYSTEM_USER_INFO_ADD = 10500;

    //角色管理 11000-11999
    int SYSTEM_ROLE_ERROR_ADD_FAIL = 11000;

    //权限管理 12000-12999
    int SYSTEM_AUTH_ERROR_ADD_FAIL = 12000;
}
