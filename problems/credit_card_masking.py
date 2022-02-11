"""
5. Hide the credit card number
Write a function in Python that accepts a credit card number. It should return
a string where all the characters are hidden with an asterisk except the last
four. For example, if the function gets sent "4444444444444444", then it should
return "4444".
"""

def mask_card(card):
    "replaces all but the last 4 digits with *"
    card = str(card)
    masked =len(card[:-4])* '*' + card[-4:]
    print(masked)

mask_card('4444444444444444')
