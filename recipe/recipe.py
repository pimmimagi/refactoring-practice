"""
Recipe for a hot beverage that the CoffeeMaker can make.
A recipe can contain coffee, sugar, milk, chocolate, and water.
Units are not specified.
"""
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    coffee: int
    chocolate: int
    milk: int
    sugar: int
    price: float


