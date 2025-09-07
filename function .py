# #function 
# def greetings():
#     num1 = input("enter first number  ")
#     num2 = input("enter second number  ")
#     print(num1 + num2)

# greetings()


# num1 = int(input("enter first number  "))
# num2 = int(input("enter second number  "))


# def add(a,b):
#     print(a + b)

# add("big","boy")

#function


# def greetings():
#     print("welcome to the application")
# greetings()


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# def add(a,b):
#     print(a + b)
# add (1, 2)


# myName = "majesty"
# myName1 = "debby"
# myName2 = "nenye"
# myName3 = "justina"
# myName4 = "despina"
# myName5 = "somto"

# def greet(*yourName):
#   print(f"hello user {yourName[3]}")
# greet(myName, myName1, myName2, myName3, myName4, myName5)


# def my_function(child1, child2, child3):
#   print("the oldest child is" + child1)
#   print("the middle child is" + child2)
#   print("the youngest child is" + child3)                                                                                                                                                                                                                                                                                                                                                                                                         


#   my_function(child2= "great", child1= "jude", child3="paschal")

# def add2(num1, num2 = 5):
#     sum = num1 + num2
#     print(f"this is the sum: {sum}")


# add2()


# bakerylist = ["bread", "cake", "donuts","cookies","muffins","strawberry cake"]


# def checkstock(pastry):
#     counter = 0
#     for item in pastry:
#         if item != "strawberry cake":
#             print("yes we have it in stock ")
#             counter += 1
#             print(counter,"loop")
#             continue
#         else:
#             print("we out of stock")
# checkstock(bakerylist)

# classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", " chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi" ]


# def check(names):
   
#     for item in names:
#         if item == "daniel":
#             print("yes i'm in class ")
#             continue 
#         else:
#             print("oops i'm not in class")
# check(classList)




"""


"""






























































#Practice time
score = 0

def quiz():
    global score

    name = input("what's your name  ").strip()
    print(f"Hello {name} your welcome to my game ")
    try:
        question = int(input("choose a question from 1-10  ").strip())
    except ValueError:
        print("Invalid selection. Please enter a number from 1 to 10.")
        return

    if question == 1:
        ans = input("what is the capital of france ").strip().lower()
        if ans == "paris":
            print("correct")
            score += 1
        else:
            print("that's incorrect; Paris is the answer")
    elif question == 2:
        ans = input("What is the capital of usa ").strip().lower()
        if ans in ("washington dc", "washington"):
            print("correct")
            score += 1
        else:
            
            print("that's incorrect; Washington DC is the answer")
    elif question == 3:
        ans = input("what is the capital of china ").strip().lower()
        if ans == "beijing":
            print("correct")
            score += 1
        else:
            print("that's incorrect; Beijing is the answer")
    elif question == 4:
        ans = input("what is the capital of india ").strip().lower()
        if ans in ("new delhi", "newdelhi"):
            print("correct")
            score += 1
        else:
            print("that's incorrect; New Delhi is the answer")
    elif question == 5:
        ans = input("what is the capital of russia ").strip().lower()
        if ans == "moscow":
            print("correct")
            score += 1
        else:
            print("that's incorrect; Moscow is the answer")
    elif question == 6:
        ans = input("what is the capital of uk ").strip().lower()
        if ans == "london":
            print("correct")
            score += 1
        else:
            print("that's incorrect; London is the answer")
    elif question == 7:
        ans = input("what is the capital of kenya ").strip().lower()
        if ans == "nairobi":
            print("correct")
            score += 1
        else:
            print("that's incorrect; Nairobi is the answer")
    elif question == 8:
        ans = input("what is the capital of egypt ").strip().lower()
        if ans == "cairo":
            print("correct")
            score += 1
        else:
            print("that's incorrect; Cairo is the answer")
    elif question == 9:
        ans = input("what is the capital of portugal ").strip().lower()
        if ans == "lisbon":
            print("correct")
            score += 1
        else:
            print("that's incorrect; Lisbon is the answer")
    elif question == 10:
        ans = input("what is the capital of mexico  ").strip().lower()
        if ans in ("mexico city", "mexicocity"):
            print("correct")
            score += 1
        else:
            print("that's incorrect; Mexico City is the answer")
    else:
        print("Invalid question number. Please choose from 1 to 10.")
        return

    print(f"Your score is: {score}")

quiz()




   






