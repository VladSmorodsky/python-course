from insufficient_funds_exception import InsufficientFundsException
from bank_account import BankAccount
from client import Client

try:
    # Add client and bank accounts
    client = Client('Test')
    bank_account_uah = BankAccount('UA1111', 500)
    bank_account_usd = BankAccount('UA1111', 0, 'USD')

    # Try to make money exchange
    client.exchange_money(bank_account_uah, bank_account_usd, 15)  # try to buy 15 USD and exception raises

    # client.exchange_money(bank_account_uah, bank_account_usd, 10)  # try to buy 10 USD
    # print(bank_account_uah.balance)
    # print(bank_account_usd.balance)
except InsufficientFundsException as exception:
    print(exception)
except Exception as exception:
    print(exception)
