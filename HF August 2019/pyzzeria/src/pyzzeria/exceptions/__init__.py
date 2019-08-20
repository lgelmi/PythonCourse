"""
Pizza Exceptions

Defines custom PizzaErrors.
"""


# __all__ = ["IngredientError"]  # This changes the import * behaviour

class PizzaError(Exception):
    """
    Generic Pizza Error.

    All PizzaError subclass this one, allowing to filter them easily.
    """
    pass


class IngredientError(PizzaError):
    """
    Pizza Error related to the ingredients.

    This is raised whenever an ingredient is missing or invalid
    """
    pass
