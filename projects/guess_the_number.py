"""Guess the number"""
from random import randint

guess = 0
numbers_used = []
generated_number = randint(1,100)
counter = 0
won = False

print("I am thinking of a number between 1 and 100")

while counter <= 10:
    if len(numbers_used) > 0:
        print(f"\nYou have guessed {numbers_used}")

    guess = input("Enter a number: ")
    if guess == 'q':
        print(f"Thanks for playing!")
        print(f"The computer's number was {generated_number}")
        break
    else:
        try:
            guess = int(guess)
        except ValueError:
            pass
        else:
            numbers_used.append(guess)
            counter +=1

            if guess == generated_number:
                break
            elif guess > generated_number:
                print("\tYour guess is too high")
            elif guess < generated_number:
                print("\tYour guess is too low")


if counter >= 10:
    print("Better luck next time")
elif guess == generated_number:
    print(f"\tYou guessed the number in {counter} attempts")
else:
    pass

