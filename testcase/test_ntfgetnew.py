# # -*- coding: utf-8 -*-
from hashlib import md5
import json
import requests
import unittest
import time
from page.sign import *
from page.ntfgetnew import *


class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json()['code'], 1)
        self.assertEqual(r.json()['http_status_code'], 201)


    def test_user_001(self):
        '''测试游戏端向商城发起nft资产创建请求，正常case'''
        args_dict = {
            "userId": "6425605781151809538",
            "id": ["e7fbda05223c57d3a3eddc61"],
            "desc": "about desc"
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/get/new', data)
        print(r.text)
        self.statusCode(r)
        time.sleep(60)

    def test_user_002(self):
        '''测试游戏端向商城发起nft资产创建请求，desc为空'''
        args_dict = {
            "userId": "6425605781151809538",
            "id": ["e7fbda05223c57d3a3eddc61"],
            "desc": ""
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/get/new', data)
        print(r.text)
        self.statusCode(r)


if __name__ == '__main__':
    unittest.main(verbosity=2)
