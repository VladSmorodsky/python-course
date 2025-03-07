import re


def validate_url(url: str) -> None:
    """
    Validate url
    :param url:
    :return:
    """
    if re.match(r"(?:https?://|www\.)[\w.\-_]+[\w/?=]+", url) is None:
        raise ValueError(f"Url is not valid: {url}")
