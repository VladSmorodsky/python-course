class InsufficientFundsException(Exception):
    """
    Throws when the issue with amount occurred
    """

    def __init__(self, required_amount: float, current_balance: float, currency: str) -> None:
        super().__init__(
            f"Insufficient Funds Exception: You have not enough balance {current_balance}{currency} to proceed with operation amount: ({required_amount}{currency})")
