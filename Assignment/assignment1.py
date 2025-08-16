"""
Ask the user for an arithmethic input 
then this code uses the the input 
"""

operation = input("Which operator do you want to use?  ")
num1 =  int(input("input a number  ") )
num2 = int(input("input a number? " ) )
if operation == '+':
    print(f"The answer of {num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f" The answer of{num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"The answer of{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    print(f"The answer of{num1} / {num2} = {num1 / num2}")
