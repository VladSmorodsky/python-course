"""
Bank account example
"""
import requests

from lesson_07_testing.task_06_complex_testing.src.exceptions.balance_error import BalanceError


class BankAccount:
    """
    Class represents bank account item
    """

    def deposit(self, amount: float) -> float:
        """
        Add money to balance
        :return:
        """
        result = requests.post('https://account.example/deposit', {'amount': amount})
        return result.json()['amount']

    def withdraw(self, amount: float) -> float:
        """
        Get money from bank account
        :return:
        """
        result = requests.post('https://account.example/withdraw', {'amount': amount})
        if result.status_code == 400:
            raise BalanceError(result.json()['error'])
        return result.json()['amount']

    def get_balance(self) -> float:
        """
        Return bank account balance
        :return:
        """
        result = requests.get('https://account.example/balance')
        return result.json()['amount']
