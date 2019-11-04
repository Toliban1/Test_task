from aiohttp import web
from app import App
from add import get_config_json

config = get_config_json('config.json')

web_Application = web.Application()
app = App()
web_Application.router.add_route('GET', '/mysql', app.get_response_mysql)
web_Application.router.add_route('POST', '/mysql', app.post_response_mysql)
web_Application.router.add_route('GET', '/redis', app.get_response_redis)
web_Application.router.add_route('POST', '/redis', app.post_response_redis)

web.run_app(web_Application, host=config['host'], port=config['port'])

