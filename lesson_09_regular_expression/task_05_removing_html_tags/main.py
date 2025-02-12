import re


def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text
    :param text:
    :return:
    """
    return re.sub(r'<.*?>', ' ', text)


if __name__ == '__main__':
    print(remove_html_tags('<html><head>Test message</head><body><p>Paragraph 1</p><p>Paragraph 2</p></body>'))
