"""
Program: Triangle Perimeter Calculator
--------------------------------------
This program prompts the user to enter the lengths of the three sides
of a triangle. It then calculates the perimeter by summing the three
side lengths and prints the result.

Example:
--------
What is the length of side 1? 3  
What is the length of side 2? 4  
What is the length of side 3? 5.5  
The perimeter of the triangle is 12.5
"""

# Solution:

def main():
    # Prompt user and read input
    side1 = float(input("What is the length of side 1? "))
    print(f"You entered: \033[1;3m{side1}\033[0m")  # Echo in bold italic

    side2 = float(input("What is the length of side 2? "))
    print(f"You entered: \033[1;3m{side2}\033[0m")

    side3 = float(input("What is the length of side 3? "))
    print(f"You entered: \033[1;3m{side3}\033[0m")

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Display the result
    print(f"The perimeter of the triangle is {perimeter}")

# Required to run main when the script is executed
if __name__ == '__main__':
    main()
