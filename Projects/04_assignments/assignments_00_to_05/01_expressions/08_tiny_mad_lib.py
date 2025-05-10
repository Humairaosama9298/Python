"""
Program: Dicesimulator rolling two dic
-----------------------
Simulates rolling two dice three times and prints each result.
Demonstrates use of loops and random number generation.

"""

# Solution:

# Import the random library
import random

# Number of sides on each die to roll
Num_sides = 8

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, Num_sides)
    die2: int = random.randint(1, Num_sides)
    total: int = die1 + die2
    print(f"Die 1 = {die1}, Die 2 = {die2}, total: {total}")

    def main():

        die = 10 

        print(f"die1 in main() start as {die1}")

        for _ in range(3):
            roll_dice()

            print

