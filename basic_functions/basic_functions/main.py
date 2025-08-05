"""
A collection of static utility functions for string and number operations.
"""

def is_anagram(string1: str, string2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(string1) == sorted(string2)

def is_palindrome(string1: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards.

    Args:
        string1 (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return string1 == string1[::-1]

def fibonacci_numbers(count: int) -> list:
    """
    Generate a list of the first 'count' Fibonacci numbers.

    Args:
        count (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the Fibonacci sequence up to 'count' numbers.
    """
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(count):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def char_frequency(input_string: str) -> dict:
    """
    Calculates the frequency of each character in the given string (case-insensitive).

    Args:
        input_string (str): The string to analyze.

    Returns:
        dict: A dictionary where the keys are characters and the values 
        are the number of times each character appears in the input string (ignoring case).

    Example:
        BasicFunctions.char_frequency('aaardvark')
        {'a': 4, 'r': 2, 'd': 1, 'v': 1, 'k': 1}
    """
    counter = {}
    for char in input_string.lower():
        counter[char] = counter.get(char, 0) + 1
    return counter

def longest_subsequent_string(input_string: str) -> str:
    """
    Finds and returns the longest substring of the input string 
    that contains no repeating characters.

    Args:
        input_string (str): The string to search within.

    Returns:
        str: The longest substring without repeating characters.
            If there are multiple substrings of the same maximum length,
            the first one encountered is returned.
    """
    longest_substring = ""
    for start_index in range(len(input_string)):
        current_substring = ""
        for character in input_string[start_index:]:
            if character in current_substring:
                break
            current_substring += character
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    return longest_substring

def check_prime(number: int) -> bool:
    """
    Determines whether the given number is a prime number.

    A prime number is a natural number greater than 1 
    that has no positive divisors other than 1 and itself.

    Args:
        number (int): The integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True

def recursive_factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.

    Raises:
        RecursionError: If the recursion depth is exceeded for very large inputs.
        ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if number == 0 else number * recursive_factorial(number - 1)

def iterative_factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer using an iterative approach.

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    total = 1
    for num in range(1, number + 1):
        total *= num
    return total

def is_leap_year(year: int) -> bool:
    """
    Determine whether a given year is a leap year.

    A year is a leap year if it is divisible by 4 but not by 100,
    except if it is divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
