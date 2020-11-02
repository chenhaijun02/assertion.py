#!/usr/bin/env python
# _*_coding:utf-8_*_
import requests,urllib3
from urllib3 import encode_multipart_formdata
from common.logs import Log

class RunMethod(object):
    """
    request
    """
    log = Log()
    urllib3.disable_warnings()


    def post_main(self,url,data,header,file=None):
        """
        post请求
        :param url:
        :param data:
        :param header:
        :param file:
        :return:
        """
        res=None
        if file!=None:
            res=requests.post(url=url,json=data,headers=header,verify=False)
        else:
            res = requests.post(url=url, json=data,headers=header, files=file, verify=False)
        return res.json()

    def get_main(self,url,header,param=None):
        """
        get请求
        :param url:
        :param header:
        :param param:
        :return:
        """
        res=None
        if param!=None:
            res=requests.get(url=url,headers=header,verify=False)
        else:
            res = requests.get(url=url, headers=header, json=param,verify=False)
        return res.json()

    def run_main(self,method,url,header,data=None,file=None):
        """
        被调用主request
        :param method:
        :param url:
        :param header:
        :param data:
        :param file:
        :return:
        """
        try:
            res=None
            if method=='post' or method=='POST' or method=='Post':
                res=self.post_main(url,data,header,file=None)
            elif method=='get' or method=='GET' or method=='Get':
                res=self.get_main(url,header,param=None)
            else:
                return "request传参错误"
            return res
        except Exception as e:
            self.log.error("请求方法报错{}".farmat(e))
if __name__ == '__main__':
    print(111)