import pytest
from source.basic_functions import is_anagram
from source.basic_functions import is_palindrome



class TestIsAnagram:
    """Test suite for the is_anagram function."""

    def test_valid_anagram(self):
        assert is_anagram('test_string', 'string_test')

    def test_non_anagram_strings(self):
        assert not is_anagram('test_string', 'test')

    def test_anagram_case_sensitivity(self):
        assert not is_anagram('Test', 'test')

    def test_invalid_argument_type_integer(self):
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

    def test_palindrome_invalid_argument_type(self):
        with pytest.raises(TypeError):
            is_palindrome(1)
