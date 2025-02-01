class InsufficientResourcesException(Exception):
    """
    Throw when player can't buy resource
    """

    def __init__(self, required_resource: str, required_amount: float, current_amount: float,
                 measure: str = 'count') -> None:
        self._required_resource = required_resource
        self._required_amount = required_amount
        self._current_amount = current_amount
        self._measure = measure

    def __str__(self) -> str:
        """Represents error message"""
        return f"Insufficient Resources {self._measure}: {self._required_resource} ({self._required_amount}). Your balance is {self._current_amount}"
