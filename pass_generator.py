import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Error: At least one character type should be selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
special_chars = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, lowercase, uppercase, digits, special_chars)

if password:
    print("Generated Password:", password)