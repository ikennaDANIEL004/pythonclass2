"""

for the third assignment
Simple Password Strength Checker

Ask user for a password
Check if it meets criteria: at least 8 characters, has uppercase, lowercase, and numbers
Use loops to count each type of character
Keep asking until they provide a strong password

"""

"""

for the third assignment
Simple Password Strength Checker

Ask user for a password
Check if it meets criteria: at least 8 characters, has uppercase, lowercase, and numbers
Use loops to count each type of character
Keep asking until they provide a strong password

"""

while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Strong password.")
        break
    else:
        print("Password must have at least one uppercase letter, one lowercase letter, and one number. Try again.")

