import logging

from aiohttp import web


class HelloController:
    """
    Represent controller with hello method
    """

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    async def hello(self, request: web.Request) -> web.Response:
        """
        Return hello message
        :param request:
        :return:
        """
        self._logger.info("Hello world request")
        return web.Response(text='Hello, World!')
