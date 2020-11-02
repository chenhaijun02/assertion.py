#!/usr/bin/env python
# _*_coding:utf-8_*_
from common.readFile import ReadFile
import pymysql
import sys
from common.logs import Log



class ExecSql(object):
    """
    执行sql语句类
    """
    log = Log()

    _instance=None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        初始化mysql配置
        :param platform_name:
        """
        #self.sql_conf = self._get_sql_conf(platform_name)
        self.sql_conf=None

    def _get_sql_conf(self, project):
        """
        获取mysql配置
        :param platform_name:
        :return:
        """
        try:
            return ReadFile().read_yaml('yaml_path')[project]['mysql']
        except:
            self.log.error("找不到对应项目：{0}".format(project))

    def connect_db(self):
        """
        连接mysql
        :return:
        """
        host = self.sql_conf['host']
        user = self.sql_conf['user']
        pwd = self.sql_conf['pwd']
        test_db = self.sql_conf['test_db']
        try:
            self.conn = pymysql.connect(host=host, user=user, password=pwd, db=test_db, port=3306, charset="utf8")
        except Exception as e:
            self.log.error("连接mysql失败：{0}".format(e))

    def get_cursor(self):
        """
        获取游标
        :return:
        """
        self.cursor=self.conn.cursor()
        return self.cursor

    def exec_sql(self,project,sql_type,sql):
        """
        执行sql语句
        :param sql_type:
        :param sql:
        :return:
        """
        self.sql_conf = self._get_sql_conf(project)
        try:
            if sql_type == 'select_one':
                self.connect_db()
                cursor = self.get_cursor()
                cursor.execute(sql)
                result = cursor.fetchone()
            elif sql_type == 'select_list':
                self.connect_db()
                cursor = self.get_cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
            elif sql_type == 'update' or sql_type == 'del' or sql_type == 'insert':
                self.connect_db()
                result = self.get_cursor().execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            return result
        except Exception as e:
            self.log.error("执行sql语句报错：{0}".format(e))


if __name__ == '__main__':
    test = ExecSql()
    a=test.exec_sql('lxk',"select_list","select t.company_name,t.name,t.type_child_name from ck_job.user_tasks u inner join ck_job.tasks t on u.task_id=t.id where u.user_id=(select user_id from ck_job.user where mobile=%s) and u.deleted_at is null order by u.created_at DESC" %18221124104)
    b=[]
    for i in a:
        for j in i:
            b.append(j)
    aaa = list(map(lambda x : x, a))
    print(a)
    print(b)
    print(aaa)