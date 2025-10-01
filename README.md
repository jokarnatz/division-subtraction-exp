# Division Subtraction Calculator

A Python project that explores division as a subtraction method using simple subtraction operations combined with a quotient counter.

## Description

This project implements division using manual subtraction instead of the built-in division operator. It demonstrates an alternative approach to division by repeatedly subtracting the divisor from the dividend and counting the number of subtractions.

## Files

- `main.py` - Main script entry point
- `operations.py` - Core division operations using subtraction method
- `helper_modules/` - Helper modules for input handling and utilities
  - `get_input.py` - Input validation and handling
  - `cls.py` - Screen clearing utility

## Usage

Run the main script:

```bash
python main.py
```

The program will prompt you for:
- Dividend (the number to be divided)
- Divisor (the number to divide by, cannot be 0)

It will then calculate the result using the subtraction method and display the execution time.

## Features

- Manual division implementation using subtraction
- Input validation with error handling
- Execution time measurement
- Handles decimal calculations