import random

print("Welcome to the game,this is a number guessing game! \n You got 7 attempt to guess the number between 1 to 100, Lets start the game.")

number_to_guess = random.randrange(1, 100)

chances:int = 7 

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess:"))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it  right!! in the {guess_counter} attempt")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops sorry, the number is {number_to_guess} better luck next time!")

    elif my_guess > number_to_guess:
        print("your guess is very high, try again!")

    elif my_guess < number_to_guess:
        print("Your guess is very low, try again!")

         
