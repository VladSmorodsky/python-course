import asyncio
import logging
from asyncio import Queue

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def produce(queue: Queue) -> None:
    """
    Produce 5 tasks and put them in a queue.
    :param queue:
    :return:
    """
    for i in range(1, 6):
        task = f"Task #{i}"
        await queue.put(task)
        logging.info(f"Added task: {task}")
        await asyncio.sleep(1)


async def consume(queue: Queue, consumer_id: int) -> None:
    """
     Emulates consuming task by consumer_id.
    :param queue:
    :param consumer_id:
    :return:
    """
    try:
        while True:
            task = await queue.get()
            logging.info(f"Consumer {consumer_id} proceeds with task: {task}")
            await asyncio.sleep(2)
            queue.task_done()
    except asyncio.CancelledError:
        logging.warning('Queue is empty. Cancelling task.')


async def main() -> None:
    """
    Add tasks into queue and create consumers for them.
    :return:
    """
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(produce(queue))
    consumers = [asyncio.create_task(consume(queue, consumer_id)) for consumer_id in range(1, 4)]
    await producer_task
    await queue.join()
    for c in consumers:
        c.cancel()
    await asyncio.gather(*consumers, )


if __name__ == "__main__":
    asyncio.run(main())
