"""
Program: Square Calculator
--------------------------
This program prompts the user to enter a number (which can be a float),
and then calculates and displays the square of that number. The square
is the number multiplied by itself.

Example:
--------
Type a number to see its square: 4  
4.0 squared is 16.0
"""

# Solution:

def main():
    # Prompt user for a number
    number = float(input("Type a number to see its square: "))

    # ANSI escape sequence for bold + italic
    styled_number = f"\033[1;3m{number}\033[0m"

    # Calculate square
    square = number * number

    # Display the result with user input in bold italic
    print(f"{styled_number} squared is {square}")

# Required to run main when the script is executed
if __name__ == '__main__':
    main()
