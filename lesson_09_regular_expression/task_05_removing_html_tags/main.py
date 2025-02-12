import re


def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text
    :param text:
    :return:
    """
    return re.sub(r'<.*?>', ' ', text)


if __name__ == '__main__':
    print(remove_html_tags('<html><head>fdfdsfa</head>fdsfadsf<body>fdsfdsaf</body>fsdfads'))
