import requests


def download_page_into_txt_file(page_url: str, file_name: str) -> None:
    """
    Stores web page into txt file
    :param page_url:
    :param file_name:
    :return:
    :raise
    """
    try:
        x = requests.get(page_url)
        with open(file_name, 'w') as text_file:
            text_file.write(x.text)
        print(f"Page {page_url} saved successfully in file {file_name}")
    except requests.exceptions.ConnectionError:
        print(f"Page {page_url} can't be reached")
    except Exception as exception:
        print(f"Something went wrong. Please check your data: {exception}")
