import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Tuple, Optional

from PIL import Image

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def resize_image(image_path: str, output_folder: str, size: Optional[Tuple[int, int]] = (100, 100)) -> None:
    """
    Process image and save it to image_path.
    :param output_folder:
    :param size:
    :param image_path:
    :return:
    """
    try:
        with Image.open(image_path) as image:
            image = image.resize(size)
            img_name = os.path.basename(image_path)
            output_path = os.path.join(output_folder, img_name)
            image.save(output_path)
            logging.info(f"Image resized: {output_path}")
    except Exception as exception:
        logging.error(f"Image not processed: {exception}")


def processing_images(image_dir: str, output_folder: str) -> None:
    """
    Process images and save them to output_folder.
    :param image_dir:
    :param output_folder:
    :return:
    """
    os.makedirs(output_folder, exist_ok=True)
    with ThreadPoolExecutor() as executor:
        for image_path in os.listdir(image_dir):
            executor.submit(resize_image, os.path.join(image_dir, image_path), output_folder, (75, 75))


processing_images('img', 'processed_images')
