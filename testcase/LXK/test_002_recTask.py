#!/usr/bin/env python
# _*_coding:utf-8_*_

import pytest
from common.readFile import ReadFile
from common.request import RunMethod
from common.assertion import Assertion
from common.execSql import ExecSql
import allure

data = ReadFile().read_excel('lxk', '推荐任务')

@pytest.mark.parametrize('function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3',data)
class Test(object):
    '''推荐任务'''


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
        pass

    def teardown_class(self):
        '''
        数据清理
        :return:
        '''
        pass

    #@allure.feature('蓝薪卡')
    @allure.story('lxk_推荐任务')
    def test_recommend_task(self,get_lxk_c_headers,function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3):
        '''
        推荐任务
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
        response_data = self.request(type,self.yaml_data['url']+url,get_lxk_c_headers)
        self.assertion.get_sql_data('lxk',eval(sql1)[0],eval(sql1)[1])
        self.assertion.get_response_data(response_data,eval(expect2))
        self.assertion.asser(function,casename,expect1,response_data,asserttype)



if __name__ == "__main__":
    pytest.main(["-s", "test_002_recTask.py"])
