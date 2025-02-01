from exception.insufficient_funds_exception import InsufficientFundsException
from model.bank_account import BankAccount
from model.client import Client

try:
    # Add client and bank accounts
    client = Client('Test')
    bank_account_uah = BankAccount('UA1111', 500)
    bank_account_usd = BankAccount('USD1111', 0, 'USD')
    client.add_bank_account(bank_account_uah)
    client.add_bank_account(bank_account_usd)

    # Try to make money exchange
    amount_to_buy = 15  # Customer wants to buy 15 USD
    bank_account_from = client.get_bank_account('UA1111')  # Get client's UAH account
    bank_account_to = client.get_bank_account('USD1111')  # Get client's USD account
    client.exchange_money(bank_account_from, bank_account_to, 15)  # try to buy 15 USD and exception raises

    # client.exchange_money(bank_account_uah, bank_account_usd, 10)  # try to buy 10 USD
    # print(bank_account_uah.balance)
    # print(bank_account_usd.balance)
except InsufficientFundsException as exception:
    print(exception)
except Exception as exception:
    print(exception)
