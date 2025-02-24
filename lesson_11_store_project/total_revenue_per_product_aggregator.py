class TotalRevenuePerProductAggregator:
    """
    This class represents the total revenue per product.
    """

    def __init__(self) -> None:
        self.total_revenue: float = 0

    def step(self, price: float, quantity: float) -> None:
        """
        This method performs the step of the total revenue calculation.
        :param price:
        :param quantity:
        :return:
        """
        self.total_revenue += price * quantity

    def finalize(self) -> float:
        """
        This method finalizes the total revenue calculation.
        :return:
        """
        return self.total_revenue
