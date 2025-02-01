from model.bank_account import BankAccount
from exception.insufficient_funds_exception import InsufficientFundsException


class ExchangeService:
    """
    Service responsible for currency exchange
    """
    __EXCHANGE_VALUE = {'UAH': {'USD': 0.02}, 'USD': {'UAH': 41.75}}

    def convert(self, amount, currency_from: str, currency_to: str) -> float:
        """
        Returns converted amount from currency_to
        :param amount:
        :param currency_from:
        :param currency_to:
        :return:
        :raise Exception
        """
        if currency_to not in self.__EXCHANGE_VALUE or currency_from not in self.__EXCHANGE_VALUE[currency_to]:
            raise Exception('Not allowed currency to exchange.')
        return round(amount * self.__EXCHANGE_VALUE[currency_to][currency_from], 2)

    def exchange(self, amount: float, bank_account_from: BankAccount, bank_account_to: BankAccount) -> None:
        """
        Exchange money according to 'amount' of 'bank_account_to' currency
        :param amount:
        :param bank_account_from:
        :param bank_account_to:
        :return:
        """
        converted_value = self.convert(amount, bank_account_from.currency, bank_account_to.currency)
        if converted_value > bank_account_from.balance:
            raise InsufficientFundsException(converted_value, bank_account_from.balance, bank_account_from.currency)
        bank_account_from.balance -= converted_value
        bank_account_to.balance += amount
