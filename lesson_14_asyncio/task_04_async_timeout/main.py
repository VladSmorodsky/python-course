import asyncio
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def slow_task(waiting_seconds: int) -> None:
    """
    Super slow task.
    :param waiting_seconds:
    :return:
    """
    logging.debug('Slow task starts...')
    await asyncio.sleep(waiting_seconds)
    logging.debug('Slow task finished!')


async def main() -> None:
    """
    Run and handle slow task.
    :return:
    """
    try:
        waiting_seconds = 10
        await asyncio.wait_for(slow_task(waiting_seconds), timeout=5)
    except asyncio.TimeoutError:
        logging.error('Task timed out.')


if __name__ == '__main__':
    asyncio.run(main())
