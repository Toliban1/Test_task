from aiohttp import web
from mysql_con import Mysql_con
from dbs import Mysql_inter, Redis_inter
import json
from redis_con import Redis_con


class App:

    def get_response_mysql(self, req):
        mysql_connecter = Mysql_con()
        text = Mysql_inter.read(mysql_connecter.open_connection())
        mysql_connecter.connection_close()
        return web.Response(status=200, text=str(text)[1:-1])

    async def post_response_mysql(self, req):
        body = await req.read()
        body = json.loads(json.loads(body.decode('utf-8')))
        mysql_con = Mysql_con()
        connection = mysql_con.open_connection()
        Mysql_inter.write(connection, body['fname'], body['iname'], body['tel'], body['email']) #, fname, iname, tel, email)
        mysql_con.connection_close()
        return web.Response(status=200, text='post')

    async def get_response_redis (self, req):
        r = Redis_con.open_connection()
        text = Redis_inter.read(r)
        return web.Response(status=200, text=text)

    async def post_response_redis(self, req):
        body = await req.read()
        body = json.loads(json.loads(body.decode('utf-8')))
        r = Redis_con.open_connection()
        body = str(body)
        Redis_inter.write(r, body)
        return web.Response(status=200, text='redis_post')


