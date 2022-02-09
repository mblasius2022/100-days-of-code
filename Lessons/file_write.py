"""
Write to a file
"""
file_name = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/programming.txt'
with open(file_name, 'w') as file_object:
    x = 0
    while x < 10:
        file_object.write("I love programming\n")
        x += 1

with open(file_name, 'a') as file_object:
    x = 0
    while x < 10:
        file_object.write("Hello World\n")
        x += 1