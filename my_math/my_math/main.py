""" 
A simple math utilities module for basic arithmetic operations.

This module provides the MyMath class, which implements static methods for
addition, subtraction, multiplication, and division of integers. All methods
are static and can be called without instantiating the class.

Example:
    from mymath import MyMath

    result_add = MyMath.add(5, 3)         # 8
    result_sub = MyMath.subtract(5, 3)   # 2
    result_mul = MyMath.multiply(5, 3)    # 15.0
    result_div = MyMath.divide(5, 2)      # 2.5
"""

class MyMath:
    """
    A utility class for basic arithmetic operations.

    Provides static methods to perform addition, subtraction, multiplication,
    and division on integer inputs.

    Functionalities:
        - Addition of two integers
        - Subtraction of two integers
        - Multiplication of two integers (returns int)
        - Division of two integers (returns float)

    Example usage:
        >>> MyMath.add(10, 5)
        15
        >>> MyMath.substract(10, 5)
        5
        >>> MyMath.multiply(10, 5)
        50.0
        >>> MyMath.divide(10, 4)
        2.5
    """

    @staticmethod
    def add(number1: int, number2: int) -> int:
        """
        Add two integers and return the sum.

        Args:
            number1 (int): The first number to add.
            number2 (int): The second number to add.

        Returns:
            int: The sum of number1 and number2.
        """
        return number1 + number2

    @staticmethod
    def subtract(number1: int, number2: int) -> int:
        """
        Subtract the second integer from the first and return the result.

        Args:
            number1 (int): The number from which to subtract.
            number2 (int): The number to subtract.

        Returns:
            int: The result of number1 minus number2.
        """
        return number1 - number2

    @staticmethod
    def multiply(number1: int, number2: int) -> float:
        """
        Multiply two integers and return the product as an int.

        Args:
            number1 (int): The first number to multiply.
            number2 (int): The second number to multiply.

        Returns:
            float: The product of number1 and number2.
        """
        return float(number1 * number2)

    @staticmethod
    def divide(number1: int, number2: int) -> float:
        """
        Divide the first integer by the second and return the result as a float.

        Args:
            number1 (int): The dividend.
            number2 (int): The divisor.

        Returns:
            float: The result of division.

        Raises:
            ZeroDivisionError: If number2 is zero.
        """
        return number1 / number2
