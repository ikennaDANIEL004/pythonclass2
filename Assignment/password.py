"""
 building a password program 
 """
def my_password():
    try:
        password = input("Enter password   ").upper()
        if password == "MR FRANK":
         print("Access given")
        else:
         print("Access denied ")
    except ValueError:
        print("invalid password")

my_password()
