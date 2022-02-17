#10.3 & 10.4
from datetime import datetime

# file = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/guest_register.txt'
# x = 0
# while x < 10 :
#     name = input("Enter your name\nEnter q to quit: ")
#     if name.lower() == 'q':
#         break
#     else:
#         # datetime object containing current date and time
#         now = datetime.now()
#         # dd/mm/YY H:M:S
#         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#         print(f"\nWelcome {name}\n")
#         with open(file, 'a') as file_object:
#             file_object.write(f"{name.title()} visited on {dt_string}\n")
#         x += 1

#10.5
# file = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/poll_results.txt'
# x = 0
# while x < 10 :
#     name = input("Enter your name\nEnter q to quit: ")
#     if name.lower() == 'q' or name == '':
#         break
#     else:
#         reason = input("Why do you like programming? ")
#         if reason != '':
#             with open(file, 'a') as file_object:
#                 file_object.write(f"{name.title()} likes progamming because {reason}\n")
#         x += 1
#10.6
# n1 = input("Enter a number: ")
# n2 = input("Enter another number: ")
# try:
#     number1 = int(n1)
#     number2 = int(n2)
# except ValueError:
#     print("one of your entries is not a number")
# else:
#     print(number1 + number2)
#10.7

# def add_numbers(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     print(f"The sum of your numbers is: {total}")

# numbers = []
# x = 0

# while x < 10:
#     n = input("Enter an number or q to quit: ")
#     if n.lower() == 'q':
#         break
#     else:
#         try:
#             number = int(n)
#         except ValueError:
#             print(f"{n} is not a number")
#         else:
#             numbers.append(number)
#             x += 1

# add_numbers(numbers)

#10.10
def count_words(file_name, word):
    """ count the approximate number of words in a text file"""
    try:
        file_path = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/'
        file_location = file_path + file_name
        with open(file_location, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Could not find file {file_name}")

    else:
        word_count = contents.count(word)
        print(f"{word} appears approx {word_count} times in {file_name}")

word_list = ['Alice', 'Mad', 'Queen', 'White Rabbit', 'heart', 'teacup']
for word in word_list:
    count_words('alice.txt', word)
