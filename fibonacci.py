#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_positive_integer():
    """Ask user for number of Fibonacci terms and validate input."""
    while True:
        user_input = input("Enter the number of Fibonacci terms: ").strip()
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Please enter a positive integer.")

def generate_fibonacci(n):
    """Generate Fibonacci sequence up to n terms and return as a list."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_sequence(sequence):
    """Print Fibonacci sequence neatly."""
    for i in range(len(sequence)):
        end_char = " " if i < len(sequence) - 1 else "\n"
        print(sequence[i], end=end_char)

def main():
    n = get_positive_integer()
    fib_sequence = generate_fibonacci(n)
    print_sequence(fib_sequence)
main()
