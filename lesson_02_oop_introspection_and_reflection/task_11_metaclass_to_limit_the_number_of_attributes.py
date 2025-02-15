class LimitedAttributesMeta(type):
    """Class is responsible for checking max class attribute's count."""
    __max_attributes_count = 3

    def __call__(cls, *args, **kwargs) -> None:
        """
        Check class attribute's count.
        :param args:
        :param kwargs:
        :return:
        """
        attr_count = 0
        for attr in cls.__dict__.keys():
            if attr_count > cls.__max_attributes_count:
                # Raise Exception if class attributes count more than acceptable
                raise Exception(f"Class {cls.__name__} can't has more than {cls.__max_attributes_count} attributes")
            if attr.startswith('__') or callable(attr):
                # Skip functions
                continue
            attr_count += 1


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Викличе помилку


obj = LimitedClass()
