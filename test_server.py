from add import make_host_url, get_config_json
from class_Test_server import Test_server

config = get_config_json('config.json')

host = make_host_url(config['host'], config['port'])

data = {'fname': 'name', 'iname': 'names', 'tel': '1234', 'email': 'mail'}

test_mode = 'post_mysql'

test_server = Test_server(host, data)
#possible test modes: 'get_mysql', 'post_mysql', 'get_redis', 'post_redis'
test_server(test_mode)








