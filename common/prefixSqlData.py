#!/usr/bin/env python
# _*_coding:utf-8_*_
from common.execSql import ExecSql
from common.readFile import ReadFile
import pytest


class MakeSqlData(object):


    exec_sql = ExecSql().exec_sql
    sql_yaml_data = ReadFile().read_yaml('sql_yaml_path')

    def __init__(self,project):
        self.project=project

    def make_sql_data(self,b_account,c_account):
        prefix_data={'user_id':''}
        print(b_account,c_account,self.project)
        company_user_id = self.exec_sql(self.project, self.sql_yaml_data[self.project]['查企业用户id'][0],self.sql_yaml_data[self.project]['查企业用户id'][1].format(b_account))[0][0]
        team_id = self.exec_sql(self.project, self.sql_yaml_data[self.project]['查团队id'][0], self.sql_yaml_data[self.project]['查团队id'][1].format(b_account))[0][0]
        user_id = self.exec_sql(self.project, self.sql_yaml_data[self.project]['查C端用户id'][0], self.sql_yaml_data[self.project]['查C端用户id'][1].format(c_account))[0][0]
        self.exec_sql(self.project, self.sql_yaml_data[self.project]['加入团队'][0], self.sql_yaml_data[self.project]['加入团队'][1].format(company_user_id,team_id,user_id,c_account))
        prefix_data['user_id']=user_id
        return prefix_data

if __name__ == "__main__":
    pytest.main(["-s", "prefixSqlData.py"])
    test1=MakeSqlData('lxk')
    print(test1.make_sql_data('18000000000','19900000000'))
