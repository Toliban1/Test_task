import json
import requests

class Test_server:

    def __init__(self, host, data):
        self.host = host
        self.data = data
        self.dict_of_modes = {
            'get_mysql': self.get_mysql,
            'post_mysql': self.post_mysql,
            'get_redis': self.get_redis,
            'post_redis': self.post_redis,
        }

    def __call__(self, test_mode):
        func = self.dict_of_modes.get(test_mode, self.dict_default)
        func()

    def get_mysql(self):
        print("test_mode == 'get_mysql'")
        response = requests.get(self.host + '/mysql')
        print('extracted data == ', response.text)

    def post_mysql(self):
        print("test_mode == 'post_mysql'")
        response = requests.get(self.host + '/mysql')
        print('1. ', response.text)
        res = requests.post(self.host + '/mysql', json=json.dumps(self.data))
        print('res = ', res)
        response = requests.get(self.host + '/mysql')
        print('2. ', response.text)

    def get_redis(self):
        print("test_mode == 'get_redis'")
        response = requests.get(self.host + '/redis')
        print('extracted data == ', response.text)

    def post_redis(self):
        print("test_mode == 'post_redis'")
        response = requests.get(self.host + '/redis')
        print('1. ', response.text)
        res = requests.post(self.host + '/redis', json=json.dumps(self.data))
        print('res = ', res)
        response = requests.get(self.host + '/redis')
        print('2. ', response.text)

    def dict_default(self):
        print('this test mode is not provided')