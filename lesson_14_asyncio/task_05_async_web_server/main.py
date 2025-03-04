import logging
import os

from aiohttp import web
from dotenv import load_dotenv

from controllers.hello_controller import HelloController
from controllers.slow_controller import SlowController

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()

server_host = os.getenv("SERVER_HOST", 'localhost')
server_port = int(os.getenv("SERVER_PORT", 8080))


async def init_app() -> web.Application:
    """
    Initialize the simple async web server
    :return:
    """
    hello_controller = HelloController(logger)
    slow_controller = SlowController(logger)

    app = web.Application()
    app.router.add_get('/', hello_controller.hello)
    app.router.add_get('/slow', slow_controller.slow)
    return app


if __name__ == '__main__':
    application = init_app()
    web.run_app(application, host=server_host, port=server_port)
