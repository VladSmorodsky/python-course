import threading
from typing import List

import requests


def download_file(url: str) -> None:
    """
    Download file from url
    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded: {file_name}")
    except Exception as e:
        print("File downloading failed:", e)


def downloading_files_by_threads(urls: List[str]) -> None:
    """
    Download file from urls using treads
    :param urls:
    :return:
    """
    threads = []

    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    urls = [
        'https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg',
        'https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg'
    ]
    downloading_files_by_threads(urls)