"""Docstring"""

class BasicFunctions:
    """Docstring"""
    
    @staticmethod
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

    @staticmethod
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


    @staticmethod
    def fibonacci_numbers(count: int) -> list:
        """
        Generate a list of the first 'count' Fibonacci numbers.

        Args:
            count (int): The number of Fibonacci numbers to generate.

        Returns:
            list: A list containing the Fibonacci sequence up to 'count' numbers.
        """
        fib_list = []
        a, b = 0, 1
        for _ in range(count):
            fib_list.append(a)
            a, b = b, a + b
        return fib_list

    @staticmethod
    def char_frequency(input_string: str) -> dict:
        """
        Calculates the frequency of each character in the given string.

        Args:
            input_string (str): The string to analyze.

        Returns:
            dict: A dictionary where the keys are characters and the values are the number of times each character appears in the input string.

        Example:
            BasicFunctions.char_frequency('aaardvark')
            {'a': 4, 'r': 2, 'd': 1, 'v': 1, 'k': 1}
        """
        counter = {}
        for char in input_string:
            counter[char] = counter.get(char, 0) + 1
        return counter

    @staticmethod
    def longest_subsequent_string(input_string: str) -> str:
        """docstring"""
        longest_substring = ""
        for char in input_string:
            if char not in longest_substring:
                longest_substring += char
        return longest_substring
