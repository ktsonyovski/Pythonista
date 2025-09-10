"""
Test the Caesar Cipher implementation.
"""
import pytest

from caeser_cipher.main import caesar_cipher


class TestCaesarCipher():
    """Test cases for the Caesar cipher function."""

    def test_cipher_encrypt_correct_input(self):
        actual_output = caesar_cipher("abc", "encrypt", 3)
        expected_output = "def"

        assert actual_output == expected_output

    def test_cipher_incorrect_input_raises_type_error(self):
        with pytest.raises(TypeError):
            caesar_cipher("missing positional arguments") # Missing args for testing

    def test_cipher_decrypt_correct_input(self):
        actual_output = caesar_cipher("def", "decrypt", 3)
        expected_output = "abc"

        assert actual_output == expected_output

    def test_cipher_non_alpha_characters(self):
        actual_output = caesar_cipher("test_string!", "encrypt", 5)
        expected_output = "yjxy_xywnsl!"

        assert actual_output == expected_output

    def test_cipher_incorrect_operation_raises_value_error(self):
        with pytest.raises(ValueError):
            caesar_cipher("abc", "invalid_operation", 3)
