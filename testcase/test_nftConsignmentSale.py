# # -*- coding: utf-8 -*-
from hashlib import md5
import json
import requests
import unittest
from page.sign import *
from page.ntfgetnew import *
import random

class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json()['code'], 1)
        self.assertEqual(r.json()['http_status_code'], 201)


    def ne_statusCode(self, r):
        '''协议状态码与业务状态码的验证'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        self.assertEqual(r.json()['http_status_code'], 200)

    def get_itemId(self):
        return random.randint(10, 1000000)

    def test_user_001(self):
        '''测试用于游戏端向商城发起nft资产挂售请求，正常case'''

        args_dict = {
            "userId": "6425591600348397569",
            "id": ["e7fbda05223c57d3a3eddc68"],
            "desc": "des",
            "price":"1"
        }

        param = {
            "sign": "e17882342f3de28bfdc2cb72105c8743",
            "args": json.dumps(args_dict).replace('"', "'")
        }


        get_sign = api_arguments_sign(param)
        print(get_sign)

        data = {"args": param["args"], "sign": get_sign}

        r = post('api/v1/nft/consignment', data)
        print(r.text)
        self.statusCode(r)




if __name__ == '__main__':
    unittest.main(verbosity=2)
