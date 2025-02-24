from sqlite3 import IntegrityError
from typing import List, Tuple

from store_project.repositories.product_repository import ProductRepository

from store_project.models.product import Product


class ProductService:
    """
    Service is responsible for working with products.
    """

    def __init__(self, product_repository: ProductRepository) -> None:
        self.__product_repository = product_repository

    def add_product(self, product: Product) -> None:
        """
        Save product into the database.
        :param product:
        :return:
        """
        try:
            self.__product_repository.add_product(product)
        except IntegrityError:
            print("Product already exists")  # log issue

    def get_available_products(self) -> List[Product]:
        """
        Get all available products.
        :return:
        """
        return self.__product_repository.get_available_products()

    def get_matched_products_from_start(self, title: str) -> List[Product] | None:
        """
        Returns all products matching the given title or part of title from start.
        :param title:
        :return:
        """
        return self.__product_repository.find_by_matching_title_from_start(title)

    def get_matched_products(self, title: str) -> List[Product] | None:
        """
        Returns all products matching the given title or part of title.
        :param title:
        :return:
        """
        return self.__product_repository.find_by_matching_title(title)

    def get_paginated_products(self, page: int = 1) -> List[Product] | None:
        """
        Returns all products matching the given page number or part of page number.
        :param page:
        :return:
        """
        if page < 1:
            page = 1
        offset_items_count = self.__product_repository.products_count_per_page * (page - 1)
        return self.__product_repository.get_paginated_products(offset_items_count)

    def get_sellable_products(self) -> List[Product] | None:
        """
        Returns all products sellable.
        :return:
        """
        return self.__product_repository.get_sellable_products()

    def get_products_with_stock_status(self) -> List[Tuple[str, str]] | None:
        """
        Returns all products with stock status.
        :return:
        """
        return self.__product_repository.get_products_with_stock_status()