"""
Positive only
Make a program that will 
Collect an int input from the user
It should also only stop running until the user gives you a negative number
"""


collect = int(input("enter a number  "))
while collect >= 0:
    print(collect)
    collect = int(input("enter a number  "))
else:
        print("Negative number entered, stopping the program.")