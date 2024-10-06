# Author: Jesse Partonen

print("I am somewhat familiar with Git")

import random as rmd

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()[]}=\`'~<>,./?"

length = int(input("Enter the length of the password: "))

all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

password = rmd.choice(lowercase_letters) + rmd.choice(uppercase_letters) + rmd.choice(numbers) + rmd.choice(special_characters)
for _ in range(length - 4):
    password += rmd.choice(all_characters)

print(password)