"""
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("Enter a word: ")
word = str(word)
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")