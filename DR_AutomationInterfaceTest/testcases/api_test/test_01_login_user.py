import pytest
import allure
from operation.login import get_user_info
from testcases.conftest import field_sql_name
from common.logger import logger
from api.ParseFile import lu

@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有用户信息")


@allure.step("步骤1 ==>> 获取某个用户信息")
def step_2(username):
    logger.info("步骤1 ==>> 获取某个用户信息：{}".format(username))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("用户管理")
@allure.feature("用户信息")
class TestLoginUser():

    @allure.story("用户登录")
    @allure.description("该用例是针对获取所有用户信息接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             lu.model_expect)
    def test_login_user(self, except_result, except_code, except_msg):
        """
        登录用户
        :return:
        """
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = get_user_info()
        # print(result.__dict__)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_login_user.py"])
