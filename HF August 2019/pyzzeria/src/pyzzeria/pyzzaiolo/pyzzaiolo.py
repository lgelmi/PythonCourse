"""
pizzaiolo.py

Define the Pyzzaiolo class, which makes pyzza.
"""
import logging

try:
    from ..magazzyno import Magazzyno
except ValueError:
    from src.pyzzeria.magazzyno import Magazzyno


class Pyzzaiolo:
    """
    Makes Pyzza.
    """
    def __init__(self, magazzyno: Magazzyno, pyzzeria: str = "Pyzzeria"):
        """
        Store the pyzzeria details and retrieve the logger.

        :param magazzyno: Magazzyno class which stores the available ingredients
        :param pyzzeria: Name of the Pyzzeria where Pyzzaiolo works
        """
        self.magazzyno = magazzyno
        # TODO: Create a Pyzzeria class
        self.pyzzeria = pyzzeria
        self.logger: logging.Logger = logging.getLogger(self.pyzzeria)

    def make_custom_pizza(self, ingredients: list):
        """
        Consume the ingredients to make Pyzza.

        Pyzza is currently an ethereal concept filled with taste.

        :param ingredients: list of ingredients needed to prepare the pizza.
        :return: Pyzza... None
        """
        self.magazzyno.consume_ingredients(ingredients)
        self.logger.info("Making Custom Pizza")
