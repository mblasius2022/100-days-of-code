"""
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they
have a “cow”. For every digit the user guessed correctly in the wrong place
is a “bull.”
"""
from random import randint

guess = 0
playing = True
random_number = str(randint(1000,9999))
print(random_number)


def compare_numbers(random_number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(random_number)):
        if random_number[i] == user_guess[i]:
            cowbull[0]+=1
        else:
            cowbull[1]+=1
    return cowbull

while playing == True:
    user_guess = str(input("enter your guess: "))
    if user_guess.lower() == 'exit':
        break

    guess += 1
    cowbull_count = compare_numbers(random_number, user_guess)
    if cowbull_count[0] ==4:
        print(f"{user_guess} is correct\nYou guessed in {guess} guesses")
        playing = False
        break
    else:
        print(f"you have {cowbull_count[0]} cows and {cowbull_count[1]} bulls")
        print("try again:\n")