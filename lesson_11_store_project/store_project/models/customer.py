from store_project.descriptors.email_descriptor import EmailDescriptor

from store_project.descriptors.phone_descriptor import PhoneDescriptor

from store_project.descriptors.name_descriptor import NameDescriptor


class Customer:
    """Represents customer data"""
    __name = NameDescriptor()
    __email = EmailDescriptor()
    __phone = PhoneDescriptor()

    def __init__(self, name: str, email: str, phone: str, customer_id: int = None, ) -> None:
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def customer_id(self) -> int | None:
        """
        Returns customer id
        :return:
        """
        return self.__customer_id

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
