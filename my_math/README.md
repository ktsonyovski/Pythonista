# my_math

A simple Python module providing basic arithmetic operations with comprehensive unit tests.

## Project Structure

my_math/<br>
├── my_math/ # Source code for the my_math module<br>
│ └── main.py # Implementation of MyMath class<br>
└── tests/ # Unit tests for the module<br>
│└── test_my_math.py

## Features

- Addition, subtraction, multiplication, and division operations
- Static methods for easy use
- Type-annotated for clarity and safety
- Comprehensive pytest-based test suite

## Usage

### Import the Module

```
from source.main import MyMath
```

### Use the Arithmetic Methods

```
result_add = MyMath.add(5, 3) # 8
result_sub = MyMath.substract(5, 3) # 2
result_mul = MyMath.multiply(5, 3) # 15.0
result_div = MyMath.divide(5, 2) # 2.5
```

## Running the Tests

This project uses [pytest](https://pytest.org/) for testing.

1. Install pytest if you haven’t already:
    ```
    pip install pytest
    ```

2. Run the tests from the `my_math` directory:
    ```
    pytest tests/
    ```

## Linting

This project is compatible with [pylint](https://pylint.org/).

To lint the source code, run:
```
pylint source/
```

> **Note:** The `tests/` folder can be excluded from linting via your `.pylintrc` configuration.
