from attack_item import AttackItem


class Sword(AttackItem):
    """
    Represents attack item: Sword
    """

    def __init__(self, name: str, price: float, attack_value: float) -> None:
        item_id = 1
        super().__init__(item_id, name, price, attack_value)
