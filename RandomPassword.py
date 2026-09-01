import random
import string

print("Random Password Generator")
try:
    length = int(input("Enter desired password length: "))
except ValueError:
    print("Invalid input! Please enter a valid integer for length.")
    exit()

print("Include the following character types? (yes/no)")
use_upper = input("Uppercase letters (A-Z): ").strip().lower() == 'yes'
use_lower = input("Lowercase letters (a-z): ").strip().lower() == 'yes'
use_numbers = input("Numbers (0-9): ").strip().lower() == 'yes'
use_special = input("Special characters (!@#$%^&* etc.): ").strip().lower() == 'yes'

char_pool = ""

if use_upper:
    char_pool += string.ascii_uppercase
if use_lower:
    char_pool += string.ascii_lowercase
if use_numbers:
    char_pool += string.digits
if use_special:
    char_pool += string.punctuation

if not char_pool:
    print("Error: No character types selected!")
    exit()

if length < 1:
    print("Error: Password length must be at least 1.")
    exit()

password = ''.join(random.choice(char_pool) for _ in range(length))

print("\nGenerated password:")
print(password)
