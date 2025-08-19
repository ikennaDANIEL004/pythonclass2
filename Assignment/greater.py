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
                

