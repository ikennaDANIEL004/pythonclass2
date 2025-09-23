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

# CORRECTION OF THE CALCULATOR CODES
                

""""""""""""""""""
""""""""""""""""""
"""
simple calculator, that gets two user int inputs and op
returns sum, diff, quotient, product
"""

#user inputs, num1 and num2
choice = "y"
while(choice == "y"):
    num1 = int(input("input your first number: "))
    num2 = int(input("enter your second number: "))

    #operation input
    op = input("enter your operation: sum \nproduct \nquotient \ndifference ").lower()

    #sum, difference, quotient, product
    def addition():
        sum = num1 + num2
        print(f"this is the sum: {sum}")

    def diff():
        difference = num1 - num2
        print(f"this is the difference of the two numbers: {difference}")

    def divide():
        quotient  = num1 / num2
        print(f"this is the quotient of two numbers: {quotient}")

    def multiply():
        product = num1 * num2
        print(f"this is the product of two numbers: {product}")


    if (op.lower() == "sum"): 
        addition()
    elif (op.lower() == "difference"):
        diff()
    elif (op.lower() == "quotient"):
        if (num2 == 0):
            print("undefined")
        else:
            divide()
    elif (op.lower() == "product"):
        multiply()
    else:
        print("invalid operator")
    
    choice = input("do you want to continue: y to continue or any other key to quit?")
    
""""
main.py
inputModule - get all the input - num1, num2, op
functionsModule - add, div, sub, mult functions
logicModule - if 



Main.py

while:
    inputModule.getnum1()
    inputModule.getnum2()
    inputModule.getOperation()

    logicModule.checkOp(op)


___________________________


inputModule.py
def getnum1()
def getnum2()
def getOperation


_____________________________

functionModule.py

def add()
def sub()
def div()
def multi()


_____________________________

logicModule.py
if(op.lower == "add"):
    functionModule.add()

""" 

