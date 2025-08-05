"""
Unit tests for the MyMath class from source.main.

This test suite verifies the correctness of all static methods in MyMath,
including addition, subtraction, multiplication, and division. It covers
various input types and edge cases to ensure robust behavior.

Example usage (with pytest):
    pytest test_mymath.py
"""

import pytest
from my_math.main import MyMath


class TestMyMath:
    """
    Test suite for the MyMath utility class.

    Contains tests for:
        - add
        - substract
        - multiply
        - divide
    """

    # Tests for add function
    def test_addition_with_valid_positive_integers(self):
        assert MyMath.add(1, 2) == 3

    def test_addition_with_negative_integers(self):
        assert MyMath.add(-3, -2) == -5

    def test_addition_float_input(self):
        assert MyMath.add(3.0, 1) == 4.0

    def test_addition_string_input(self):
        assert MyMath.add("test", " string") == "test string"

    def test_addition_with_zero(self):
        assert MyMath.add(2, 0) == 2

    # Tests for subtract function
    def test_subtract_with_positive_integers(self):
        assert MyMath.subtract(5, 2) == 3

    def test_subtract_with_negative_result(self):
        assert MyMath.subtract(2, 5) == -3

    def test_subtract_with_zero(self):
        assert MyMath.subtract(0, 0) == 0

    def test_subtract_with_floats(self):
        assert MyMath.subtract(5.5, 2.5) == 3.0

    # Tests for multiply function
    def test_multiply_with_positive_integers(self):
        assert MyMath.multiply(3, 4) == 12.0

    def test_multiply_with_zero(self):
        assert MyMath.multiply(0, 5) == 0.0

    def test_multiply_with_negative_integer(self):
        assert MyMath.multiply(-2, 3) == -6.0

    def test_multiply_with_floats(self):
        assert MyMath.multiply(2.5, 2) == 5.0

    # Tests for divide function
    def test_divide_with_positive_integers(self):
        assert MyMath.divide(10, 2) == 5.0

    def test_divide_resulting_in_float(self):
        assert MyMath.divide(7, 2) == 3.5

    def test_divide_with_negative_numbers(self):
        assert MyMath.divide(-8, 2) == -4.0

    def test_divide_with_floats(self):
        assert MyMath.divide(5.0, 2) == 2.5

    def test_divide_by_one(self):
        assert MyMath.divide(9, 1) == 9.0

    def test_divide_by_negative_one(self):
        assert MyMath.divide(9, -1) == -9.0

    def test_divide_zero_by_integer(self):
        assert MyMath.divide(0, 5) == 0.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            MyMath.divide(5, 0)
