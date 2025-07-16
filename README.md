# Password Generator and Checker

A simple Python tool for generating secure passwords and checking password strength.

## Features

- **Generate passwords** with customizable length
- **Check password strength** with detailed feedback
- **No external dependencies** - uses only Python standard library

## Usage

### Generate a Password

```python
from password_tool import generate_password

# Generate a 12-character password (default)
password = generate_password()
print(password)  # Example: "Kp9!mXz2Qw8@"

# Generate a 16-character password
long_password = generate_password(16)
print(long_password)  # Example: "Rt7#nM4!vBx9Kz2@"
```

### Check Password Strength

```python
from password_tool import check_password

result = check_password("MyPassword123!")
print(f"Strength: {result['strength']}")  # Strong
print(f"Score: {result['score']}/5")      # 5/5

# Check a weak password
weak_result = check_password("password")
print(f"Strength: {weak_result['strength']}")  # Weak
print("Suggestions:", ", ".join(weak_result['feedback']))
```

## Password Requirements

The strength checker evaluates passwords based on:

1. **Length**: At least 8 characters
2. **Lowercase letters**: a-z
3. **Uppercase letters**: A-Z
4. **Numbers**: 0-9
5. **Special characters**: !@#$%^&*()_+-=[]{}|;:,.<>?

## Strength Ratings

- **Strong** (4-5 criteria met): Excellent security
- **Good** (3 criteria met): Adequate for most uses
- **Fair** (2 criteria met): Needs improvement
- **Weak** (0-1 criteria met): Not recommended

## Installation

No installation required! Just download the script and run:

```bash
python password_tool.py
```

## Example Output

```
Generated password: Kp9!mXz2Qw8@
Strength: Strong (5/5)

Testing 'password123':
Strength: Fair (2/5)
Suggestions: Add uppercase letters, Add special characters
```

## Security Notes

- Generated passwords use Python's `random` module, suitable for most purposes
- For cryptographic applications, consider using `secrets` module instead
- Always store passwords securely (hashed, not plain text)
- Don't reuse passwords across different accounts

## License

Free to use and modify as needed.
