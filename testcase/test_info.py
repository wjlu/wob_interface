#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
from page.info import *
import time as t
# 创建一个测试类
class InfoTest(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass



    def test_info_001(self):
        '''资料业务：测试感情状态功能是否可编辑'''
        data = {'profile': 1, 'albumId': -1, 'photoId': 0, 'photoUrl': '', 'loveInfoId': 0,
                'yScale': 0, 'loveType': 1, 'withName': '', 'withId': '', 'fromYear': 0, 'fromMonth': 0,
                'fromDay': 0, 'submit': '保存', 'requestToken': -704754670, '_rtk': "a1bf4a6c"}
        r = post('http://www.renren.com/loveinfo/update?v=info_timeline', data)
        print(r.text)

        str1 = r.text
        self.assertTrue('单身' in str1)


if __name__=='__main__':
    unittest.main(verbosity=2)
