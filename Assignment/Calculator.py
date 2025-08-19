"""
Ask the user for an arithmethic input 
then this code uses the the input 
"""

operation = input("Which operator do you want to use SUM, MULTIPLY, SUBTRACT, DIVIDE? ")
num1 =  int(input("input a number  ") )
num2 = int(input("input a number? " ) )
if operation.lower() == 'sum':
    print(f"The answer of {num1} + {num2} = {num1 + num2}")
elif operation.lower() == 'subtract':
    print(f" The answer of {num1} - {num2} = {num1 - num2}")
elif operation.lower() == 'multiply':
    print(f"The answer of {num1} * {num2} = {num1 * num2}")
elif operation.lower() == 'divide':
    print(f"The answer of {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator")

print("Thank you for using the calculator")

#  


