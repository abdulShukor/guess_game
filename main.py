
"""Guess number """

import random

def guess(number):
    random_number= random.randint(1,number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number 1 and {number}: "))
        if guess < random_number:
            print("Sorry, quess again. Too low.")
        elif guess > random_number:
            print("Sorry, quess again. Too low")

    print(f"Yeah, congrats, You have guessed the number {random_number}. correctly!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c': # feedback != 'c' and  low != high 
        if low != high:
            guess =  random.randint(low, high)
        else:
            guess =  low # could be also high becuse low = high (will not loop through when low = high)
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        print(f"Yeah, The computer guessed your number guessed, {guess}. correctly!!")


#guess(10)
computer_guess(10)