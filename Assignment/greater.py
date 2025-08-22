# This function gives the greater of two numbers 

def number():
    try:
        num1 = int(input("Enter a number "))
        num2 = int(input("Enter a number "))
        if num1 > num2 :
            print(f"{num1} is greater thats why its printed out ")
        else:
            print(f"{num2} is greater thats why its printed out ")

    except ValueError:
        print("this is not even neccessary ")

number()


num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
if (num1 == num2 ):
    print("the numbers are the same ")
elif (num1 < num2):
    print(f"num2: {num2} is the greater number")
else:
    print(f"num1: {num1} is the greater ")
