class BankAccount:
    """
    Represents bank account
    """

    def __init__(self, bank_account_id: str, amount: float = 0, currency='UAH'):
        self.__bank_account_id = bank_account_id
        self.__balance = amount
        self.__currency = currency

    @property
    def bank_account_id(self) -> str:
        """
        Returns bank id
        :return:
        """
        return self.__bank_account_id

    @property
    def balance(self) -> float:
        """
        Get account amount
        :return:
        """
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Set bank account amount
        :param value:
        :return:
        """
        self.__balance = value

    @property
    def currency(self) -> str:
        """
        Get account currency
        :return:
        """
        return self.__currency

    def __repr__(self) -> str:
        """
        Represents bank account info
        :return:
        """
        return f"(bank_id: {self.__bank_account_id}, balance: {self.__balance}, currency: {self.__currency})"
