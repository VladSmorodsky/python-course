"""
Test BankAccount class
"""
from unittest.mock import patch, Mock

import pytest

from ..src.bank_account import BankAccount
from ..src.exceptions.balance_error import BalanceError


@pytest.fixture
def bank_account_fixture():
    return BankAccount()


class TestBankAccount:

    @pytest.mark.parametrize("added_amount, expected_amount", [
        (10, 20),
        (20, 30)
    ])
    @patch('src.bank_account.requests.post')
    def test_deposit_method(self, mocked_method, bank_account_fixture, added_amount, expected_amount):
        """
        Test deposit with bank account fixture, mocked post request method and parameters
        :param mocked_method:
        :param bank_account_fixture:
        :param added_amount:
        :param expected_amount:
        :return:
        """
        # Mock endpoint
        expected_result = {"amount": expected_amount}
        mocked_method.return_value.json.return_value = expected_result
        mocked_method.return_value.status_code = 201
        # Add money to account
        result = bank_account_fixture.deposit(added_amount)
        # Assert
        assert expected_amount == result

    @pytest.mark.parametrize("withdraw_amount, expected_amount", [
        (10, 20),
        pytest.param(
            0, 1, marks=pytest.mark.skip(reason="Skip testing when withdraw equals 0.")
        ),
        (20, 30),
    ])
    @patch('src.bank_account.requests.post')
    def test_withdraw_method(self, mocked_post_method, bank_account_fixture, withdraw_amount, expected_amount):
        # Mock endpoint
        expected_result = {"amount": expected_amount}
        mocked_post_method.return_value.json.return_value = expected_result
        mocked_post_method.return_value.status_code = 200
        result = bank_account_fixture.withdraw(withdraw_amount)
        # Assert
        assert result == expected_amount

    @patch('src.bank_account.requests.post')
    def test_withdraw_method_raise_balance_error(self, mocked_post_method, bank_account_fixture):
        """
        Test withdraw method raises BalanceError when not enough money on balance
        :param mocked_post_method:
        :param bank_account_fixture:
        :return:
        """
        # Mock endpoint
        withdraw_amount = 20.99
        expected_result = {"error": "Not enough money"}
        mocked_post_method.return_value.json.return_value = expected_result
        mocked_post_method.return_value.status_code = 400
        with pytest.raises(BalanceError, match="Not enough money"):
            bank_account_fixture.withdraw(withdraw_amount)

    @patch('src.bank_account.requests.get')
    def test_get_balance_method(self, mocked_get_method, bank_account_fixture):
        """
        Test get balance method with mocked get method and bank account fixture
        :param bank_account_fixture:
        :return:
        """
        # Mock endpoint
        expected_result = {"amount": 10}
        mocked_get_method.return_value.json.return_value = expected_result
        result = bank_account_fixture.get_balance()
        # Assert
        assert 10 == result
