"""
Program: Fahrenhite to Celsius Converter
----------------------------------------
This program prompts the user to enter a temperature in Fahrenhite, then converts and display it in celsuis using the formula:
     degrees_celsuis = (degrees_fahrenhite - 32) * 5.0 / 9.0

""" 

# Solution:


def main():
    # Prompt user to enter temperature in fahrenhite
    fahrenhite = float(input("Enter temperature in fahrenhite: "))

    # Convert to celsuis using the correct formula
    celsuis = (fahrenhite - 32) * 5.0 / 9.0

    # Display result with both F and C values
    print(f"Temperature: {fahrenhite}F = {celsuis}C")


if __name__ == "__main__":
    main()