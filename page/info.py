#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
from page.login import *
def post(url,data):
    '''
    对post请求二次封装
        para
    '''
    r = login().post(url=url,data=data,timeout=6)
    return r
