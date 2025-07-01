"""Test cases for all the functions present in the basic_functions module."""
import pytest
from source.basic_functions import is_anagram
from source.basic_functions import is_palindrome
from source.basic_functions import fibonacci_numbers
from source.basic_functions import char_frequency
from source.basic_functions import check_prime


class TestIsAnagram:
    """Test suite for the is_anagram function."""

    def test_valid_anagram(self):
        assert is_anagram('test_string', 'string_test')

    def test_non_anagram_strings(self):
        assert not is_anagram('test_string', 'test')

    def test_anagram_case_sensitivity(self):
        assert not is_anagram('Test', 'test')

    def test_invalid_argument_type_integer_raises_type_error(self):
        with pytest.raises(TypeError):
            is_anagram('test', 1)


class TestPalindrome:
    """Test suite for the is_palindrome function."""

    def test_palindrome_valid(self):
        assert is_palindrome('racecar')

    def test_palindrome_invalid(self):
        assert not is_palindrome('test_string')

    def test_palindrome_list(self):
        assert is_palindrome(['r', 'a', 'c', 'e', 'c', 'a', 'r'])

    def test_palindrome_case_sensitivity(self):
        assert not is_palindrome('Racecar')

    def test_palindrome_invalid_argument_type_raises_type_error(self):
        with pytest.raises(TypeError):
            is_palindrome(1)


class TestFibonacci:
    """Test suite for the fibonacci_numbers function."""

    def test_fibonacci_valid(self):
        expected_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci_numbers(10) == expected_output

    def test_fibonacci_zero_input(self):
        assert fibonacci_numbers(0) == []

    def test_invalid_fibonacci_input_raises_type_error(self):
        with pytest.raises(TypeError):
            assert fibonacci_numbers('test')

    def test_fibonacci_float_input_raises_type_error(self):
        with pytest.raises(TypeError):
            fibonacci_numbers(5.5)


class TestCharFrequency:
    """Test suite for the char_frequency function."""

    def test_valid_frequency_case(self):
        assert char_frequency('aardvark') == {'a': 3, 'r': 2, 'd': 1, 'v': 1, 'k': 1}

    def test_case_insensitivity(self):
        assert char_frequency('Test') == {'e': 1, 's': 1, 't': 2}

    def test_char_frequency_raises_attribute_error_with_invalid_input(self):
        with pytest.raises(AttributeError):
            char_frequency(1)


class TestCheckPrime:
    """Test suite for the check_prime function."""

    def test_valid_positive_integer(self):
        assert check_prime(11)

    def test_valid_false_positive_integer(self):
        assert not check_prime(12)

    def test_invalid_negative_integer_input(self):
        assert not check_prime(-12)

    def test_with_zero_input(self):
        assert not check_prime(0)

    def test_invalid_string_input_raises_type_error(self):
        with pytest.raises(TypeError):
            check_prime("test")
