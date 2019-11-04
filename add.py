import json

def make_host_url(host, port):
    return 'http://{}:{}'.format(host, port)
def get_config_json(file_name):
    with open(file_name) as file:
        return json.load(file)

