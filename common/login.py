#!/usr/bin/env python
# _*_coding:utf-8_*_
from common import request
from common.readFile import ReadFile
from common.logs import Log


class Login(object):
    """
    登录
    """
    log = Log()
    request = request.RunMethod()

    def __init__(self):
        self.yaml_data = ReadFile().read_yaml('yaml_path')['lxk']
        self.header = self.yaml_data['headers']
        self.url = self.yaml_data['url']
        self.lxk_c_url = self.yaml_data['c_login']['url']
        self.lxk_c_method = self.yaml_data['c_login']['method']
        self.lxk_c_param = self.yaml_data['c_login']['param']


    def lxk_c_login(self,project,mobile):
        """
        蓝薪卡C端登录
        :param project:
        :param mobile:
        :return:
        """
        try:
            if project=='lxk_c':
                self.lxk_c_param['mobile']=mobile
                result=self.request.run_main(self.lxk_c_method, self.url+self.lxk_c_url, self.header, self.lxk_c_param)
            elif project=='lxk_a':
                pass
            elif project=='lxk_b':
                pass
            return result
        except Exception as e:
            self.log.error('登录报错{}'.format(e))

if __name__ == '__main__':
    test=Login()
    print(test.lxk_c_login('lxk_c','18221124104'))
