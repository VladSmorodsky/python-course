import re


def pick_hashtags(text: str) -> list[str]:
    """
    Get all hashtags from text.
    Example: Introduce #hashtag_picker! It helps to identify #companies, #people, #places around the #World!
    Result: ['#hashtag_picker', '#companies', '#people', #places, '#World']
    :param text:
    :return:
    """
    return re.findall(r'#\w+', text)


if __name__ == '__main__':
    print(pick_hashtags('Introduce #hashtag_picker! It helps to identify #companies, #people, #places around the #World!'))
