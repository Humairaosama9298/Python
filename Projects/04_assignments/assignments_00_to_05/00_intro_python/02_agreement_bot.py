"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
"""
# Solution:

def main():
    # Step 1: Ask user for their favorite animal
    animal = input("What's your favorite animal ____? ")

    # Step 2: User input is in bold and italic and \033[1;3m Starts bold and italic text, \033[0m resets style
    print(f"My favorite animal is also \033[1;3m {animal}\033[0m!")

if __name__ == "__main__":
    main()