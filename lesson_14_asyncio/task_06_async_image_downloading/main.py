import asyncio
import logging
import os
from urllib.parse import urlparse

import aiohttp

from models.image import Image

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def download_image(image: Image) -> None:
    """
    Download image from url
    :param image:
    :return:
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image.url) as response:
                response.raise_for_status()
                image_data = await response.read()
                if image_data is None:
                    raise ValueError('Response is empty.')
                image_extension = _get_image_extension(image.url)
                _validate_image_extension(image_extension)
                with open(f"{image.name}{image_extension}", 'wb') as file:
                    file.write(image_data)
                logger.info(f'Image downloaded: {image.name}{image_extension}')
    except aiohttp.ClientConnectorError:
        logger.error(f"Cannot connect to {image.url}.")
    except aiohttp.ClientResponseError as e:
        logger.error(f"Error response from {image.url}: {e.status} - {e.message}")
    except ValueError as e:
        logger.error(f"Error response from {image.url}: {e}")


def _get_image_extension(url: str) -> str:
    """
    Get image extension from url
    :param url:
    :return:
    """
    parsed_url = urlparse(url)
    path = parsed_url.path
    _, ext = os.path.splitext(path)
    return ext if ext else None


def _validate_image_extension(image_extension: str) -> None:
    """
    Validate if image extension is valid
    :param image_extension:
    :return:
    """
    allowed_extensions = ['jpg', 'jpeg', 'png']
    if image_extension[1:] not in allowed_extensions:
        raise ValueError(f'Image extension must be one of {allowed_extensions}')


async def main() -> None:
    """
    Run image downloading tasks
    :return:
    """
    try:
        image_list = [
            Image('https://djeqr6to3dedg.cloudfront.net/repo-logos/library/python/live/logo-1720462259584.png',
                  'python'),
            Image('https://djeqr6to3dedg.cloudfront.net/repo-logos/library/docker/live/logo-1739383862625.png',
                  'docker'),
            Image('https://quintagroup.com/cms/js/js-image/javascript-logo.png', 'js')
        ]
        await asyncio.gather(*[download_image(image) for image in image_list])
    except ValueError as e:
        logger.error(f'Error downloading image: {e}')


if __name__ == '__main__':
    asyncio.run(main())
