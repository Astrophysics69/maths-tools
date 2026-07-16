"""
Unit tests for easy_to_maths package.
Run with: pytest tests/test_maths.py -v
"""

import pytest
from easy_to_maths import (
    addition,
    subtraction,
    multiplication,
    division,
    modulus,
    floor_division,
)


class TestArithmetic:
    """Test suite for arithmetic operations."""

    def test_addition(self):
        """Test addition function."""
        assert addition(2, 3) == 5
        assert addition(0, 0) == 0
        assert addition(-5, 5) == 0
        assert addition(1.5, 2.5) == 4.0

    def test_subtraction(self):
        """Test subtraction function."""
        assert subtraction(10, 4) == 6
        assert subtraction(0, 0) == 0
        assert subtraction(-5, -3) == -2
        assert subtraction(5.5, 2.5) == 3.0

    def test_multiplication(self):
        """Test multiplication function."""
        assert multiplication(6, 7) == 42
        assert multiplication(0, 100) == 0
        assert multiplication(-3, 4) == -12
        assert multiplication(2.5, 2) == 5.0

    def test_division(self):
        """Test division function."""
        assert division(20, 4) == 5.0
        assert division(10, 2) == 5.0
        assert division(-20, 4) == -5.0
        assert division(5, 2) == 2.5

    def test_division_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            division(10, 0)

    def test_modulus(self):
        """Test modulus function."""
        assert modulus(17, 5) == 2
        assert modulus(10, 3) == 1
        assert modulus(20, 5) == 0
        assert modulus(-17, 5) == 3

    def test_modulus_by_zero(self):
        """Test modulus by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            modulus(10, 0)

    def test_floor_division(self):
        """Test floor division function."""
        assert floor_division(17, 5) == 3
        assert floor_division(20, 4) == 5
        assert floor_division(-17, 5) == -4
        assert floor_division(7, 2) == 3

    def test_floor_division_by_zero(self):
        """Test floor division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            floor_division(10, 0)


class TestEdgeCases:
    """Test edge cases and special values."""

    def test_large_numbers(self):
        """Test with large numbers."""
        assert addition(10**10, 10**10) == 2 * 10**10
        assert multiplication(10**5, 10**5) == 10**10

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert addition(-5, -3) == -8
        assert multiplication(-4, -5) == 20
        assert division(-20, -4) == 5.0

    def test_float_precision(self):
        """Test float operations."""
        result = addition(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10  # Account for floating-point precision
