import uuid
from uuid import UUID


class UniqueIdGenerator:
    """Class generates unique id"""

    def __iter__(self) -> 'UniqueIdGenerator':
        """
        Returns UniqueIdGenerator object
        :return UniqueIdGenerator:
        """
        return self

    def __next__(self) -> 'UUID':
        """
        Returns uuid object
        :return:
        """
        return uuid.uuid4()


id_generator = UniqueIdGenerator()

for _ in range(0, 5):
    print(next(id_generator))
