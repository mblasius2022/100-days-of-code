"""
read file
"""
file_path = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/'
file_name = 'pi_digits.txt'
file_location = file_path + file_name
with open(file_location) as file_object:
    contents = file_object.read()
print(contents)

with open(file_location) as file_object:
    lines = file_object.readlines()

with open(file_location) as file_object:
    for line in file_object:
        print(line.rstrip())

file_path = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/'
file_name = 'pi_to_one_million_digits.txt'
file_location = file_path + file_name
with open(file_location) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter birthday in ddmmyy: ")
if birthday in pi_string:
    print ("Your birthday appears in the  first million digits of pi")
else:
    print ("Your birthday does not appear in the first million digits of pi")