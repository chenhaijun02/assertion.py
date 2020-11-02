#!/usr/bin/env python
# _*_coding:utf-8_*_
import pytest,os,allure
if __name__ == "__main__":

    pytest.main(['-s',''])
    #生成测试报告json
    pytest.main(["-s", "-q", '--alluredir', 'C:/Users/wangli/PycharmProjects/PytestAutomation/report/result'])
    #将测试报告转为html格式
    split='allure '+'generate '+'C:/Users/wangli/PycharmProjects/PytestAutomation/report/result '+'-o '+'C:/Users/wangli/PycharmProjects/PytestAutomation/report/html '+'--clean'
    os.system('cd C:/Users/wangli/PycharmProjects/PytestAutomation/report')
    os.system(split)
    print(split)

