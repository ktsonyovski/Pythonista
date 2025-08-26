# Caesar Cipher

A simple Python implementation of the classic Caesar cipher for encrypting and decrypting text messages.

## Features

- Encrypt and decrypt text using Caesar cipher technique
- Interactive command-line interface
- Preserves non-alphabetic characters (spaces, punctuation, etc.)

## Usage

### Interactive Mode

Run the program directly for an interactive experience:

```bash
python main.py
```

The program will prompt you for:
1. Operation type ('encrypt' or 'decrypt')
2. Text to process
3. Shift number (integer)

### Programmatic Usage

```python
from ceaser_cipher.main import caesar_cipher

# Encrypt a message
encrypted = caesar_cipher("hello world", "encrypt", 3)
print(encrypted)  # Output: "khoor zruog"

# Decrypt a message
decrypted = caesar_cipher("khoor zruog", "decrypt", 3)
print(decrypted)  # Output: "hello world"
```

## Examples

### Basic Encryption/Decryption
```bash
$ python main.py
What operation to do ('encrypt' or 'decrypt'): encrypt
Please provide text to encrypt/decrypt: hello world
Enter shift number: 3
khoor zruog
```

### Mixed Case and Special Characters
```bash
$ python main.py
What operation to do ('encrypt' or 'decrypt'): encrypt
Please provide text to encrypt/decrypt: hello, world!
Enter shift number: 5
mjqqt, btwqi!
```

## Project Structure

```
ceaser_cipher/
├── ceaser_cipher/
│   └── main.py          # Main implementation
├── resources/
│   └── alphabet.json    # Alphabet configuration
└── README.md           # This file
```