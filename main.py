#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Shuffling the lists first
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

#getting the letters based on user input
letters_p = ""
for letter in letters:
  if len(letters_p) < nr_letters:
    letters_p += letter

new_password = letters_p

#getting the numbers 
numbers_p = ""
for num in numbers:
  if len(numbers_p) < nr_numbers:
    numbers_p += num

new_password += numbers_p

#getting the symbols
symbols_p = ""
for symbol in symbols:
  if len(symbols_p) < nr_symbols:
    symbols_p += symbol

#Shuffling the password
new_password += symbols_p
pswrd = [char for char in new_password]
random.shuffle(pswrd)

rand_pass = ""
for l in pswrd:
  rand_pass += l

#printing password
print(f"Your new password is: {rand_pass}")




