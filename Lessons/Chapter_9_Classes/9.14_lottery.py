"""
A basic lottery simulator
"""

from random import choice, randint

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]
possibilities = []
winning_ticket = []
random_ticket = []

def generate_winning_ticket():

    while len(winning_ticket) < 4 :
        selected_item = choice(possibilities)

        if selected_item not in winning_ticket:
            winning_ticket.append(selected_item)

    return winning_ticket



def select_possibilities():
    x = 0
    while x < 10:
        number = randint(1,40)
        if number not in possibilities:
            possibilities.append(number)
            x += 1


def select_lottery_letters():
    y = 0
    while y < 5:
        letter = choice(alphabet)
        if letter not in possibilities:
            possibilities.append(letter)
            y += 1

def get_my_ticket():
    while len(random_ticket) < 4:
        possibility = choice(possibilities)
        if possibility not in random_ticket:
            random_ticket.append(possibility)
    return random_ticket

def check_ticket(my_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    #   winning ticket, return False.
    for element in my_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True


select_possibilities()
select_lottery_letters()

winning_ticket = generate_winning_ticket()


print(f"Winning Ticket = {winning_ticket}")

plays = 0
won = False
max_tries = 1000000

while won == False:
    my_ticket = get_my_ticket()

    won = check_ticket(my_ticket, winning_ticket)
    plays += 1

    if plays >= max_tries:
        break


if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
