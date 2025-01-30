from bank_account import BankAccount
from exchange_service import ExchangeService


class Client:
    """
    Represents bank client
    """
    __bank_accounts: dict[str, BankAccount]

    def __init__(self, name: str):
        self.__name = name
        self.__exchange_service = ExchangeService()

    def get_bank_account(self, bank_account_id: str) -> BankAccount:
        """
        Return BankAccount
        :param bank_account_id:
        :return:
        """
        if self.__bank_accounts[bank_account_id] is None:
            raise Exception('Bank account not found.')
        return self.__bank_accounts[bank_account_id]

    def set_bank_account(self, bank_account: BankAccount) -> None:
        """
        Set new bank account
        :param bank_account:
        :return:
        """
        if bank_account.bank_account_id in self.__bank_accounts:
            raise Exception(f"Bank account is already exist.")
        self.__bank_accounts[bank_account.bank_account_id] = bank_account

    def exchange_money(self, bank_account_from: BankAccount, bank_account_to: BankAccount, amount: float) -> None:
        self.__exchange_service.exchange(amount, bank_account_from, bank_account_to)
