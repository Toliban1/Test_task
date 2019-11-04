import redis
from add import get_config_json


class Redis_con:

    config = get_config_json('config_redis.json')

    def open_connection():
        pool = redis.ConnectionPool(host=Redis_con.config['host'],
                                    port=Redis_con.config['port'],
                                    db=Redis_con.config['db'])
        r = redis.Redis(connection_pool=pool)
        return r

    # закрытие соединения по данным из интернета не требуется
