import re

from ..exceptions.template_mismatch_error import TemplateMismatchError


class Validation:
    """
    responsible for validating rules
    """

    def is_empty(self, value: str) -> None:
        """
        Validates empty string
        :param value:
        :return:
        """
        if len(value) == 0:
            raise ValueError('Value cannot be an empty string.')

    def is_year(self, year: str) -> None:
        """
        Validates year value
        :param year:
        :return:
        """
        if re.match(r"^[0-9]{4}$", year) is None:
            raise TemplateMismatchError("Year has to be a 4 digit number.")
