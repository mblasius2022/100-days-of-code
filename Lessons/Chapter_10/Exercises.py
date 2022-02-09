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
file = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/poll_results.txt'
x = 0
while x < 10 :
    name = input("Enter your name\nEnter q to quit: ")
    if name.lower() == 'q' or name == '':
        break
    else:
        reason = input("Why do you like programming? ")
        if reason != '':
            with open(file, 'a') as file_object:
                file_object.write(f"{name.title()} likes progamming because {reason}\n")
        x += 1
