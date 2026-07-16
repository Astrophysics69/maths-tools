"""
easy-to-maths: A simple Python package for basic arithmetic operations.

This package provides simple, efficient implementations of common mathematical
operations including addition, subtraction, multiplication, division,
modulus, and floor division.

Example:
    >>> import easy_to_maths
    >>> easy_to_maths.addition(5, 3)
    8
    >>> easy_to_maths.multiplication(6, 7)
    42
"""

from .maths import (
    addition,
    division,
    floor_division,
    modulus,
    multiplication,
    subtraction,
)

__version__ = "0.4.0"
__author__ = "Arpit Soni"
__email__ = "harshit998ops@gmail.com"
__license__ = "MIT"
__description__ = "A simple Python package providing basic arithmetic operations."

__all__ = [
    "addition",
    "subtraction",
    "multiplication",
    "division",
    "modulus",
    "floor_division",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]
