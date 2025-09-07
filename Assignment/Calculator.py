"""
Ask the user for an arithmethic input 
then this code uses the the input 
"""

# while True:
#     operation = input("Which operator do you want to use SUM, MULTIPLY, SUBTRACT, DIVIDE? ")
#     num1 =  int(input("input a number  ") )
#     num2 = int(input("input a number? " ) )
#     if operation.lower() == 'sum':
#         print(f"The answer of {num1} + {num2} = {num1 + num2}")
#     elif operation.lower() == 'subtract':
#         print(f" The answer of {num1} - {num2} = {num1 - num2}")
#     elif operation.lower() == 'multiply':
#         print(f"The answer of {num1} * {num2} = {num1 * num2}")
#     elif operation.lower() == 'divide':
#         print(f"The answer of {num1} / {num2} = {num1 / num2}")
#     # elif num1 or num2 != int:
#     #     break
#     elif operation != "sum" or "subtract" or "multiply" or "didvide":
#         print("this is not an operator")
#         break
#     else:
#         print("Invalid operator")
#     choose = input("Do you want to continue y/n ")
#     if choose == "y":
#         continue
#     elif choose == "n":
#         break



#     print("Thank you for using the calculator")
    



def quiz():
        name = input("what is your name ")
        pick = input(f"pick a number from 1-3 {name} ")
        while True:
            if pick == 1:
             ask = input("what is the capital of usa")
            if ask == "washington DC ":
                print("your correct")
            else:
                print("your wrong its washington DC")

quiz()
                

    