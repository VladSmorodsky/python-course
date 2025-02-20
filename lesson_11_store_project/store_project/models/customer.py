from store_project.descriptors.email_descriptor import EmailDescriptor


class Customer:
    """Represents customer data"""
    __email = EmailDescriptor()

    def __init__(self, name: str, email: str, phone: str) -> None:
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def name(self) -> str:
        """
        Returns the name of the customer.
        :return:
        """
        return self.__name

    @property
    def email(self) -> str:
        """
        Returns the email of the customer.
        :return:
        """
        return self.__email

    @property
    def phone(self) -> str:
        """
        Returns the phone of the customer.
        :return:
        """
        return self.__phone
