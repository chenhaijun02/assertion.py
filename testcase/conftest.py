#!/usr/bin/env python
# _*_coding:utf-8_*_
import pytest,os,yaml,requests
from common.readFile import ReadFile
from common.login import Login

yaml_data=ReadFile().read_yaml('yaml_path')

@pytest.fixture(scope='session')
def get_lxk_c_headers():
    """
    登录获取token更新headers
    :return:
    """
    headers=yaml_data['lxk']['headers']
    token=Login().lxk_c_login('lxk_c',yaml_data['lxk']['account']['c_account'])['data']['token']
    headers['Authorization']=token
    return headers





