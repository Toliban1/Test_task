import pymysql.cursors
from add import get_config_json

class Mysql_con:

    def open_connection(self):
        self.config = get_config_json('config_mysql.json')
        self.connection = pymysql.connect(host=self.config["host"],
                                          port=self.config["port"],
                                          user=self.config["user"],
                                          password=self.config["password"],
                                          db=self.config["db"],
                                          charset=self.config["charset"],
                                          cursorclass=pymysql.cursors.DictCursor)
        return self.connection

    def connection_close(self):
        self.connection.commit()
        self.connection.close()
        return True
