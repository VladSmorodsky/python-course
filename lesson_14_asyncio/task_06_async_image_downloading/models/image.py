from descriptors.url_descriptor import UrlDescriptor

from descriptors.name_descriptor import NameDescriptor


class Image:
    """
    Represents image object.
    """
    _url = UrlDescriptor()
    _name = NameDescriptor()

    def __init__(self, image_url: str, image_name: str) -> None:
        self._url = image_url
        self._name = image_name

    @property
    def url(self) -> str:
        return self._url

    @property
    def name(self) -> str:
        return self._name
