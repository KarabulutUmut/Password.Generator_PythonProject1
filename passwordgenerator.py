import string
import random

def generate(length, digits=True, letters=True, specials=True):
    to_use = []
    pwd = ""

    if digits:
        to_use += list(string.digits)
    if letters:
        to_use += list(string.ascii_letters)
    if specials:
        to_use += list(string.punctuation)

    if length_in < 1:
        raise ValueError("The length of your password cant be less than 1")
    if not to_use:
        raise ValueError("At least one charachter type needed!")

    for x in range(length):
        to_add = random.choice(to_use)
        pwd += to_add

    return pwd

length_in = int(input("Enter the length of your desired password: "))
digits_in = input("Do you want digits/numbers in your password? (y/n)").lower() == "y"
letters_in = input("Do you want letters in your password? (y/n)").lower() == "y"
specials_in = input("Do you want special characters in your password? (y/n)").lower() == "y"
password = generate(length_in, digits_in, letters_in, specials_in)
print(password)