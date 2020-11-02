#!/usr/bin/env python
# _*_coding:utf-8_*_

import pytest
from common.readFile import ReadFile
from common.request import RunMethod
from common.assertion import Assertion
from common.execSql import ExecSql
from common.prefixSqlData import MakeSqlData
import allure

data = ReadFile().read_excel('lxk', '我的报名')
print(data)

# @pytest.mark.parametrize('function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3',data)
# class Test(object):
#     '''我的报名'''
#
#     request = RunMethod().run_main
#     assertion = Assertion()
#     exec_sql = ExecSql().exec_sql
#     yaml_data = ReadFile().read_yaml('yaml_path')['lxk']
#     sql_yaml_data = ReadFile().read_yaml('sql_yaml_path')['lxk']
#     prefix_sql_data = MakeSqlData('lxk').make_sql_data
#
#
#     def setup_class(self):
#         '''
#         数据初始化
#         :return:
#         '''
#         prefix_data=self.prefix_sql_data(self.yaml_data['account']['b_account'], self.yaml_data['account']['c_account'])
#         company_id = self.exec_sql('lxk', self.sql_yaml_data['查企业id'][0], self.sql_yaml_data['查企业id'][1].format(self.yaml_data['account']['b_account']))[0][0]
#         task_id = self.exec_sql('lxk', self.sql_yaml_data['查任务id'][0], self.sql_yaml_data['查任务id'][1].format(self.yaml_data['account']['b_account']))[0][0]
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'],1))
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'],2))
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'],3))
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'],4))
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'],5))
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'],7))
#         self.exec_sql('lxk', self.sql_yaml_data['报名任务'][0], self.sql_yaml_data['报名任务'][1].format(prefix_data['user_id'], task_id, company_id,self.yaml_data['account']['c_account'], 8))
#
#     def teardown_class(self):
#         '''
#         数据清理
#         :return:
#         '''
#         self.exec_sql('lxk', self.sql_yaml_data['删除已报名任务'][0], self.sql_yaml_data['删除已报名任务'][1].format(self.yaml_data['account']['c_account']))
#         self.exec_sql('lxk', self.sql_yaml_data['解除用户团队'][0], self.sql_yaml_data['解除用户团队'][1].format(self.yaml_data['account']['c_account']))
#
#     #@allure.feature('蓝薪卡')
#     @allure.story('lxk_我的报名')
#     def test_apply_task(self,get_lxk_c_headers,function,casename,type,run,url,hearders,param,sql1,sql2,sql3,asserttype,expect1,expect2,expect3):
#         '''
#         我的报名
#         :param get_lxk_c_headers:
#         :param function:
#         :param casename:
#         :param type:
#         :param run:
#         :param url:
#         :param hearders:
#         :param param:
#         :param sql1:
#         :param sql2:
#         :param sql3:
#         :param asserttype:
#         :param expect1:
#         :param expect2:
#         :param expect3:
#         :return:
#         '''
#         response_data = self.request(type,self.yaml_data['url']+url,get_lxk_c_headers,eval(param))
#         self.assertion.get_sql_data('lxk',eval(sql1)[0],eval(sql1)[1].format(self.yaml_data['account']['c_account']))
#         self.assertion.get_response_data(response_data,eval(expect2))
#         self.assertion.asser(function,casename,expect1,response_data,asserttype)
#
#
#
# if __name__ == "__main__":
#     pytest.main(["-s", "test_001_applyTask.py"])








