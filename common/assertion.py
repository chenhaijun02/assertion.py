#!/usr/bin/env python
# _*_coding:utf-8_*_
from common.execSql import ExecSql
from common.logs import Log

class Assertion(object):
    log=Log()
    sql_values_list = []
    response_values = []

    def __init__(self):
        self.test=ExecSql().exec_sql

    def get_sql_data(self,project,sql_type,sql):
        '''
        查询sql数据组合list
        :param project:
        :param sql_type:
        :param sql:
        :return:
        '''
        try:
            sql_values=self.test(project,sql_type,sql)
            for i in sql_values:
                for j in i:
                    self.sql_values_list.append(j)
        except Exception as e:
            self.log.error("查询sql数据组合list报错{}".format(e))


    def get_response_data(self,response_data, keys=[]):
        '''
        获取接口响应数据组合list
        :param response_data:
        :param keys:
        :return:
        '''
        try:
            if isinstance(response_data, list):
                for value in response_data:
                    if isinstance(value, list) or isinstance(value, dict):
                        self.get_response_data(value, keys)
            elif isinstance(response_data, dict):
                for i, j in sorted(response_data.items()):
                    if i in keys:
                        self.response_values.append(j)
                    else:
                        self.get_response_data(j, keys)
            else:
                pass
        except Exception as e:
            self.log.error("获取接口响应数据组合list报错{}".format(e))

    def asser(self,function,casename,expect,response_data,assert_type=None):
        '''
        断言
        :param assert_type:
        :param expect:
        :param response_data:
        :return:
        '''
        try:
            if assert_type=='type1':
                assert self.sql_values_list==self.response_values
                self.log.info("查询sql数据组合list为{}".format(self.sql_values_list))
                self.log.info("接口响应数据组合list为{}".format(self.response_values))
            assert eval(expect)['code'] == response_data['code']
            assert eval(expect)['msg'] == response_data['msg']
            self.log.info("{}——{}【PASS】".format(function,casename))
        except Exception as e:
            self.log.error("{}——{}【PASS】{}".format(function,casename,e))

if __name__ == '__main__':
    # sql="select t.company_name,t.name,t.type_child_name from ck_job.user_tasks u inner join ck_job.tasks t on u.task_id=t.id where u.user_id=(select user_id from ck_job.user where mobile=18221124104) and u.deleted_at is null order by u.created_at DESC"
    #
    # test=Assertion()
    # test.get_sql_data(self,project,sql_type,sql)
    self.log.error("查询sql数据组合list报错{}".format(e))