# Adults only
"""
Make a program that will keep running until the user gives an age that is above 18
"""

age = int(input("Enter your age: "))
while age != 18:
    print("Access denied. You must be over 18.")
    age = int(input("Enter your age: "))
print("Access granted.")

