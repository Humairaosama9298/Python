"""
Program: add2numbers
--------------------
This program prompts the user to enter two integer values.
It then converts the inputs to integers, calculates their sum,
and displays the total with an appropriate message.
"""


# Solution:

def main():
    # Step 1: Prompt user to enter the first number
    first_input = input("Enter the first number: ")

    # Step 2: Convert input to integer
    first_number = int(first_input)

    # Step 3: Prompt user to enter the second number
    second_input = input("Enter the second number: ")

    # Step 4: Convert input to integer
    second_number = int(second_input)

    # Step 5: Calculate the sum
    total = first_number + second_number

    # Step 6: Display the result
    print(f"The sum of {first_number} + {second_number} = {total}")


if __name__ == "__main__":
    main()