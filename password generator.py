import random

def generate_password(length, number):
  """Generates a specified number of secure passwords with the given length."""

  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

  for _ in range(number):
    password = ""
    for _ in range(length):
      character = random.choice(characters)
      password += character
    print(password)

# Get user input for password length and number
desired_length = int(input("Enter the desired password length: "))
num_passwords = int(input("Enter the number of passwords to generate: "))

# Generate and print the passwords
generate_password(desired_length, num_passwords)