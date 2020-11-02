#!/usr/bin/env python
# _*_coding:utf-8_*_

import pytest
from common.readFile import ReadFile
from common.request import RunMethod
from common.assertion import Assertion
from common.execSql import ExecSql
from common.prefixSqlData import MakeSqlData
import allure

data = ReadFile().read_excel('lxk', '实名绑卡')

@pytest.mark.parametrize('function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3',data)
class Test(object):
    '''实名绑卡'''


    request = RunMethod().run_main
    assertion = Assertion()
    exec_sql = ExecSql().exec_sql
    yaml_data = ReadFile().read_yaml('yaml_path')['lxk']
    sql_yaml_data = ReadFile().read_yaml('sql_yaml_path')['lxk']
    prefix_sql_data = MakeSqlData('lxk').make_sql_data


    def setup_class(self):
        '''
        数据初始化
        :return:
        '''
        self.prefix_sql_data(self.yaml_data['account']['b_account'], self.yaml_data['account']['c_account'])
        self.exec_sql('lxk', self.sql_yaml_data['清除实名绑卡'][0], self.sql_yaml_data['清除实名绑卡'][1].format(self.yaml_data['account']['c_account']))
        self.exec_sql('lxk', self.sql_yaml_data['清除实名绑卡'][0], self.sql_yaml_data['清除实名绑卡'][2].format(self.yaml_data['account']['c_account']))

    def teardown_class(self):
        '''
        数据清理
        :return:
        '''
        self.exec_sql('lxk', self.sql_yaml_data['清除实名绑卡'][0], self.sql_yaml_data['清除实名绑卡'][1].format(self.yaml_data['account']['c_account']))
        self.exec_sql('lxk', self.sql_yaml_data['清除实名绑卡'][0], self.sql_yaml_data['清除实名绑卡'][2].format(self.yaml_data['account']['c_account']))
        self.exec_sql('lxk', self.sql_yaml_data['解除用户团队'][0], self.sql_yaml_data['解除用户团队'][1].format(self.yaml_data['account']['c_account']))


    #@allure.feature('蓝薪卡')
    @allure.story('lxk_实名绑卡')
    def test_set_password(self,get_lxk_c_headers,function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3):
        '''
        实名绑卡
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
    pytest.main(["-s", "test_005_bindBank.py"])
