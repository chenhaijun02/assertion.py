#!/usr/bin/env python
# _*_coding:utf-8_*_

import pytest
from common.readFile import ReadFile
from common.request import RunMethod
from common.assertion import Assertion
from common.execSql import ExecSql
import allure

data = ReadFile().read_excel('lxk', '设置登录密码')

@pytest.mark.parametrize('function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3',data)
class Test(object):
    '''设置登录密码'''


    request = RunMethod().run_main
    assertion = Assertion()
    exec_sql = ExecSql().exec_sql
    yaml_data = ReadFile().read_yaml('yaml_path')['lxk']
    sql_yaml_data = ReadFile().read_yaml('sql_yaml_path')['lxk']


    def setup_class(self):
        '''
        数据初始化
        :return:
        '''
        self.exec_sql('lxk', self.sql_yaml_data['清除登录密码'][0], self.sql_yaml_data['清除登录密码'][1].format(self.yaml_data['account']['c_account']))

    def teardown(self):
        '''
        数据清理
        :return:
        '''
        self.exec_sql('lxk', self.sql_yaml_data['清除登录密码'][0], self.sql_yaml_data['清除登录密码'][1].format(self.yaml_data['account']['c_account']))

    #@allure.feature('蓝薪卡')
    @allure.story('lxk_设置登录密码')
    def test_set_password(self,get_lxk_c_headers,function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3):
        '''
        设置登录密码
        :param get_lxk_c_headers:
        :param function:
        :param casename:
        :param type:
        :param run:
        :param url:
        :param hearders:
        :param param:
        :param sql1:
        :param sql2:
        :param sql3:
        :param asserttype:
        :param expect1:
        :param expect2:
        :param expect3:
        :return:
        '''
        response_data = self.request(type, self.yaml_data['url'] + url, get_lxk_c_headers, eval(param))
        self.assertion.asser(function,casename,expect1,response_data)


if __name__ == "__main__":
    pytest.main(["-s", "test_004_setPassword.py"])
