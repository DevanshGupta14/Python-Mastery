# Password Generator

A Python program that generates secure random passwords based on user preferences.

## Features

- User-defined password length
- Choose whether to include:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Random password generation
- Input validation using `try-except`
- Option to generate multiple passwords
- Prevents invalid inputs

## Concepts Used

- Variables
- Strings
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Input validation
- `try-except`
- Python Standard Library
  - `random`
  - `string`

## How to Run

```bash
python3 password_generator.py
```

## Sample Output

```
Enter password length: 12

Include uppercase? (y/n): y
Include lowercase? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
A@9dk!Q8m#P2
```

## Future Improvements

- Password strength indicator
- Copy password to clipboard
- Save generated passwords to a file
- Exclude confusing characters (O, 0, l, I)

## Author

Devansh Gupta