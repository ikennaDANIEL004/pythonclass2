"""
this is a Gaming program 
"""
def Gaming():
    try:
        number = int(input("input a number "))
        if number % 2 == 0:
            print(f"{number} is even number")
        elif number % 2 == 1 :
             print(f" {number} is an odd number")
        else:
            print("Please enter a valid integer.")
    except ValueError:
        print("plese enter a valid number")

Gaming()

      
