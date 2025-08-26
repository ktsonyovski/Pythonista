"""Caesar cipher implementation.
This module provides functionality to encrypt and decrypt text using the Caesar cipher technique.
It reads the alphabet from a JSON file and allows users to specify the shift amount."""
import json
from pathlib import Path

def _load_alphabet() -> list[str]:
    """Load alphabet from JSON file with robust path resolution."""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    alphabet_path = script_dir.parent / "resources" / "alphabet.json"
    
    try:
        with open(alphabet_path, encoding="utf-8") as f:
            return json.load(f)["alphabet"]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Alphabet file not found at {alphabet_path}") from e

def caesar_cipher(input_string: str, operation: str, shift: int) -> str:
    """
    Applies a Caesar cipher to the input string.

    Parameters:
        input_string (str): The text to encrypt or decrypt.
        operation (str): Either 'encrypt' or 'decrypt' to specify the action.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The encrypted or decrypted string.
    
    Raises:
        ValueError: If operation is not 'encrypt' or 'decrypt'.
    """
    if operation not in ("encrypt", "decrypt"):
        raise ValueError("Operation must be 'encrypt' or 'decrypt'")
    
    alphabet = _load_alphabet()
    result = ""
    shift_amount = shift if operation == "encrypt" else -shift
    
    for char in input_string:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift_amount) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char

    return result

def main() -> str:
    """Main function to run the Caesar cipher program.
    It prompts the user for input and displays the result.
    
    Returns:
        str: The result of the cipher operation.
    """
    chosen_operation = input("What operation to do ('encrypt' or 'decrypt'): ").strip().lower()
    user_input = input("Please provide text to encrypt/decrypt: ").strip().lower()
    try:
        shift_number = int(input("Enter shift number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer number.")
        return ""
    return caesar_cipher(user_input, chosen_operation, shift_number)

if __name__ == "__main__":
    print(main())