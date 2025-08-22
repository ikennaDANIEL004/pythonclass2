"""
Simple yes or no
Keep asking the user if he wants to continue
They should choose between y or n
If y. Then keep running the program
If n then break and end the program

"""

yes = "y"
no = "n"
while True:
    choose = input("choose between yes or no: ").lower()
    if choose == "y":
        print(True)
    elif choose == "n":
        break

