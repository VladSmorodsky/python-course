import asyncio
import logging

from aiohttp import web


class SlowController:
    """
    Represents controller with slow responses
    """

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    async def slow(self, request: web.Request) -> web.Response:
        """
        Get response after 5 seconds emulating operation
        :param request:
        :return:
        """
        self._logger.info("Received request for /slow - starting long operation")
        await asyncio.sleep(5)
        self._logger.info("Completed long operation for /slow")
        return web.Response(text="Operation completed")
