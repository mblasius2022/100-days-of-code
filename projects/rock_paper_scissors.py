""" simple rock paper scissors game"""
from random import choice

def play():

    """ controls how the game is played"""
    options = ['r', 'p', 's']
    computer_choice = choice(options)

    player_choice = input("\nEnter 'r' for rock 'p' for paper 's' for scissors: ")

    if player_choice == computer_choice:
        print("\tIt's a tie")
    elif is_win(player_choice, computer_choice):
         print("\tYou Won")
    else:
        print("\tYou lost")



def is_win(p, c):
    """ r>s, s>p, p>r
    return True if player wins"""
    if (p == 'r' and c == 's') or (p == 's' and c == 'p')  or\
    (p == 'p' and c == 'r'):
        return True

play_game = True

while play_game == True:
    play_again = input("\nDo you want to play y or n: ")
    if play_again == 'y':
        play()
    else:
        play_game = False
        print("\tMaybe some other time")

