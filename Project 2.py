import random
import string

print("--- Simple Password Generator ---")

small_letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all_characters = small_letters + capital_letters + numbers + symbols

# Desired password length from the user
while True:
    try:
        length_str = input("How long should the password be? (e.g., 12): ")
        password_length = int(length_str)
        if password_length <= 0:
            print("Please enter a positive number for length.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Password generation 
new_password = ""
for _ in range(password_length):
    random_char = random.choice(all_characters)
    new_password += random_char # Add the chosen character to the password

# Display password
print(f"\nYour new password is: {new_password}")
print("--- Generation Complete ---")
