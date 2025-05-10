"""
Program: Age Solver
--------------------------
This program solves an age-related riddle involving five friends:
Anton, Beth, Chen, Drew, and Ethan.

- Anton is 21 years old.
- Beth is 6 years older than Anton.
- Chen is 20 years older than Beth.
- Drew is as old as Chen's age plus Anton's age.
- Ethan is the same age as Chen.

The program calculates each person's age
and prints the names and their ages.
"""

# Solution:

def main():
    # Storing Anton's age
    Anton = 21

    # Beth is 6 years older than Anton
    Beth = Anton + 6

    # Chen is 20 years older than Beth
    Chen = Beth + 20

    # Drew is as old as Chen's age plus Anton's age
    Drew = Chen + Anton

    # Ethan is the same age as Chen
    Ethan = Chen

    # Printing names and ages (Capitalization and punctuation matters)
    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")

# Required to run main() when the script is executed
if __name__ == "__main__":
    main()
