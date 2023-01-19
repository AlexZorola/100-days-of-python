import random

#List of the alphabet to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#List of numbers to be used in the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#List of Symbols to be used in the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Prompt the user for the proper information to generate a random password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Generate a list based on the user inputs
password_list = []

#Insert random letters from the list into the password list being generated
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

#Insert random symbol from the list into the password list being generated
for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

#Insert random number from the list into the password list being generated
for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

#Shuffle the list in order to randomize it
random.shuffle(password_list)

#Traverse the list and print the password
password = ""
for character in password_list:
    password += character
print(f"Your password is: {password}")