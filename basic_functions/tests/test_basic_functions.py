"""Test cases for all the functions present in the basic_functions module."""
import pytest
from basic_functions.main import is_anagram
from basic_functions.main import is_palindrome
from basic_functions.main import fibonacci_numbers
from basic_functions.main import char_frequency
from basic_functions.main import longest_subsequent_string
from basic_functions.main import check_prime
from basic_functions.main import iterative_factorial
from basic_functions.main import recursive_factorial
from basic_functions.main import is_leap_year


class TestIsAnagram:
    """Test suite for the is_anagram function."""

    def test_valid_anagram_returns_true(self):
        assert is_anagram('test_string', 'string_test')

    def test_non_anagram_returns_false(self):
        assert not is_anagram('test_string', 'test')

    def test_is_anagram_case_sensitivity(self):
        assert not is_anagram('Test', 'test')

    def test_anagram_raises_type_error_with_invalid_type(self):
        with pytest.raises(TypeError):
            is_anagram('test', 1)


class TestPalindrome:
    """Test suite for the is_palindrome function."""

    def test_valid_palindrome_returns_true(self):
        assert is_palindrome('racecar')

    def test_non_palindrome_returns_false(self):
        assert not is_palindrome('test_string')

    def test_palindrome_list_returns_true(self):
        assert is_palindrome(['r', 'a', 'c', 'e', 'c', 'a', 'r'])

    def test_palindrome_is_case_sensitive(self):
        assert not is_palindrome('Racecar')

    def test_palindrome_raises_type_error_with_invalid_type(self):
        with pytest.raises(TypeError):
            is_palindrome(1)


class TestFibonacci:
    """Test suite for the fibonacci_numbers function."""

    def test_fibonacci_with_valid_input(self):
        expected_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci_numbers(10) == expected_output

    def test_fibonacci_with_zero_returns_empty(self):
        assert fibonacci_numbers(0) == []

    def test_fibonacci_raises_type_error_with_invalid_type(self):
        with pytest.raises(TypeError):
            fibonacci_numbers('test')

    def test_fibonacci_with_float_raises_type_error(self):
        with pytest.raises(TypeError):
            fibonacci_numbers(5.5)


class TestCharFrequency:
    """Test suite for the char_frequency function."""

    def test_char_frequency_with_valid_string(self):
        assert char_frequency('aardvark') == {'a': 3, 'r': 2, 'd': 1, 'v': 1, 'k': 1}

    def test_char_frequency_is_case_insensitive(self):
        assert char_frequency('Test') == {'e': 1, 's': 1, 't': 2}

    def test_char_frequency_raises_attribute_error_with_invalid_input_type(self):
        with pytest.raises(AttributeError):
            char_frequency(1)


class TestLongestSubstring:
    """Test suite for the longest_subsequent_string function."""

    def test_longest_subsequent_string_with_valid_input(self):
        assert longest_subsequent_string('test_string') == '_string'

    def test_longest_subsequent_string_with_empty_string(self):
        assert longest_subsequent_string("") == ""

    def test_longest_subsequent_string_with_invalid_type_raises_type_error(self):
        with pytest.raises(TypeError):
            longest_subsequent_string(1)


class TestCheckPrime:
    """Test suite for the check_prime function."""

    def test_valid_prime_number_returns_true(self):
        assert check_prime(11)

    def test_non_prime_number_returns_false(self):
        assert not check_prime(12)

    def test_negative_number_returns_false(self):
        assert not check_prime(-12)

    def test_check_prime_with_zero_returns_false(self):
        assert not check_prime(0)

    def test_check_prime_with_invalid_type_raises_type_error(self):
        with pytest.raises(TypeError):
            check_prime("test")


class TestRecursiveFactorial:
    """Test suite for the recursive_factorial function."""

    def test_recursive_factorial_with_valid_input(self):
        assert recursive_factorial(5) == 120

    def test_recursive_factorial_with_zero_returns_one(self):
        assert recursive_factorial(0) == 1

    def test_recursive_factorial_with_negative_input_raises_value_error(self):
        with pytest.raises(ValueError):
            recursive_factorial(-1)

    def test_recursive_factorial_with_invalid_type_raises_type_error(self):
        with pytest.raises(TypeError):
            recursive_factorial("test")


class TestIterativeFactorial:
    """Test suite for the iterative_factorial function."""

    def test_iterative_factorial_with_valid_input(self):
        assert iterative_factorial(5) == 120

    def test_iterative_factorial_with_zero_returns_one(self):
        assert iterative_factorial(0) == 1

    def test_iterative_factorial_with_negative_input_raises_value_error(self):
        with pytest.raises(ValueError):
            iterative_factorial(-1)

    def test_iterative_factorial_with_invalid_type_raises_type_error(self):
        with pytest.raises(TypeError):
            iterative_factorial("test")


class TestLeapYear:
    """Test suite for the is_leap_year function."""

    def test_year_divisible_by_4_returns_true(self):
        assert is_leap_year(2024)

    def test_year_divisible_by_400_returns_true(self):
        assert is_leap_year(2000)

    def test_year_not_divisible_by_4_returns_false(self):
        assert not is_leap_year(2025)

    def test_year_divisible_by_100_not_400_returns_false(self):
        assert not is_leap_year(1900)

    def test_year_with_invalid_type_raises_type_error(self):
        with pytest.raises(TypeError):
            is_leap_year("test")
