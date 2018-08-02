#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

import  requests
import  os

def getHeaders():
	'''获取请求头信息'''
	headers={
	'Content-Type':'application/x-www-form-urlencoded',
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
	}
	return headers

def post(url,data):
	'''
	对post请求进行二次封装
	:parameter url:请求地址
	:parameter data:请求参数
	'''
	r=requests.post(url=url,json=data,timeout=6,headers=getHeaders())
	return r

def dir_base(fileName):
	'''
	实现文件的读写
	:parameter fileName:文件的名称
	'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),'data',fileName)
