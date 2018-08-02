#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018611738162'
data={'email':'lwj.198@163.com','icode':'','origURL':'http://www.renren.com/home','domain':'renren.com','key_id':1,
      'captcha_type':'web_login','password':'2efb86f376255fe05fa460427e0bffb27253eafd602e3daf6667fa9f37bf4389',
      'rkey':'81a9d7f881711911a2ddf0fbc5f82a9c','f':'http%3A%2F%2Fzhibo.renren.com%2Ftop'}


def login():
	s=requests.Session()
	r=s.post(url=url,data=data)
	return s


