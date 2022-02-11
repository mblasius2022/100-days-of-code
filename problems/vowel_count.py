"""
4. Count the vowels in a string
Create a function in Python that accepts a single word and returns the number
of vowels in that word. In this function, only a, e, i, o, and u will be
counted as vowels — not y.
"""

def count_vowels(word):
    """ count the number of vowels in the string provided """
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    characters = list(word)

    for character in characters:
       if character in vowels:
           vowel_count += 1

    return vowel_count

text = "Create a function in Python that accepts a single word"
word_list = text.split(' ')
for word in word_list:
    vowel_count = count_vowels(word)
    print(f"{word} has {vowel_count} vowels")






