class CounterLimitContextManager:
    """Context manager is used for limiting infinite loop"""

    def __init__(self, current_number: int, limit_number=100) -> None:
        self._current_number = current_number
        self._limit_number = limit_number

    def __enter__(self) -> int:
        """
        Return the current number when entering into the context
        :return int:
        """
        return self._current_number

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop iterating after current_number >= limit_number
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        if self._current_number >= self._limit_number:
            raise ValueError()
