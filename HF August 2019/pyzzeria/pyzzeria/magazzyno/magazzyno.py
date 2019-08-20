"""
magazzyno.py

Define the Magazzyno class
"""
import logging

try:
    from ..exceptions import *
except ValueError:
    from pyzzeria import *

class Magazzyno:
    """
    Stores ingredients and... others.
    """

    name = "DaName"
    """
    This is just an attribute to show the docstring
    """

    def __init__(self, ingredients: dict, pyzzeria: str = "Pyzzeria"):
        """
        Initialize the ingredient dictionary.

        :param ingredients: Initial ingredients in the magazzyno.
        """
        self.ingredients: dict = ingredients
        self.pyzzeria = pyzzeria
        self.logger: logging.Logger = logging.getLogger(self.pyzzeria)

    def add_ingredient(self, ingredient: str, amount: int):
        """
        Add the given ingredient to the magazzyno.

        :param ingredient: ingredient to be added.
        :param amount: quantity to be added.
        """
        try:
            self.ingredients[ingredient] += amount
        except KeyError:
            self.ingredients[ingredient] = amount

    def check_ingredients(self, checked: list):
        """
        Checks that all the given ingredients are available.

        :param checked: ingredients to be checked.
        :return: list of missing ingredients.
        """
        # TODO: allow a variable amount of ingredients
        return [ingredient for ingredient in checked if
                ingredient not in self.ingredients or self.ingredients[ingredient] <= 0]

    def consume_ingredients(self, consumed: list):
        # TODO: allow a variable amount of ingredients
        missing_ingredients = self.check_ingredients(consumed)
        if missing_ingredients:
            raise IngredientError("We're out of %s" % missing_ingredients)
        else:
            for ingredient in consumed:
                self.ingredients[ingredient] -= 1
