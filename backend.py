import random
import string

def generate_password(length, use_numbers, use_symbols):

    characters = string.ascii_letters  # a-zA-Z

    if use_numbers:
        characters += string.digits  # 0-9

    if use_symbols:
        characters += string.punctuation  # !@#$%

    password = ''.join(random.choice(characters) for i in range(length))

    return password


def check_strength(password):

    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"