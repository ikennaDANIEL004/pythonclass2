"""
For the first assignment
Grade Calculator

Ask user for their score (0-100)
Assign letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
Provide encouraging messages based on the grade
Handle invalid input (scores outside 0-100 range)



"""

def grade_calculator():
    score = int(input("enter your score   "))
    if score < 0 or score > 100:
        print("invalid score, please enter your score again")
    elif score >= 90:
        print("A thats an excellent score!")
    elif score > 80 and  score < 89:
        print("B  good job")
    elif score > 70 and  score < 79:
        print("C  you can do better")
    elif score > 60 and score < 69: 
        print("D Better grades next time ")
    elif score < 60:
        print("F is not a good score ")
    else:
        print("thats not even a score ")


grade_calculator()
        


