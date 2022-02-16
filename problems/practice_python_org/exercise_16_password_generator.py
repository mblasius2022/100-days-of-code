"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating a
new password every time the user asks for a new password. Include your
run-time code in a main method."""
from random import choice
import string

def main():
    char = string.ascii_letters + string.digits + string.punctuation
    weak_passwords = ("poppy", "balloon", "detectives", "scarlett")
    x = 0
    password = ""

    password_strength = input("Password strength - Enter Weak or Strong: ")
    if password_strength == "weak":
        password = choice(weak_passwords)
    else:
        length = input("Enter length of required password:")
        length = int(length)

        while x < length:
            password = password + choice(char)
            x += 1

    print(f"password = {password}")

    another = input("Generate another password y or n: ")
    if another.lower() == "y":
        main()
    else:
        print("OK ... maybe next time")




if __name__ == "__main__":
    main()