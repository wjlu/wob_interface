import requests
from page.user  import *
import unittest

class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data ={
            "csrf_token":"ImI4NzU4NzgzYWUzM2I3N2UwMzYxM2MxNjA3YjUyY2QwOGI2NzUyNjIi.DkHNMQ.FOZXILm5JEf6vYMFE1yejiUikM8",
            "email":"lwj.198@163.com",
            "password":"030618aaa"}

        r = post("http://47.75.105.222/login",data=data)
        print(r.cookies['session'])
        print('我执行了。。。')
        with open(dir_base('token'),'w') as f:
            f.write(r.cookies['session'])

    def getToken(self):
        '''获取token'''
        with open(dir_base('token'),'r') as f:
            return f.read()


    def test_user_001(self):
        '''登录业务'''

if __name__ == '__main__':
    unittest.main(verbosity=2)
