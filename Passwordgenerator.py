import random
import string

def generate_password(length=5):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password of length 5
print(generate_password())
