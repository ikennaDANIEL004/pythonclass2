# dog 
# costructor - name,breed
# method bark - park "woof""woof"
# 

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("donny","german sherperd")
print(my_dog.name)
print(my_dog.breed)  
print(my_dog.bark())



print("########################")


class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def meow(self):
        print("meow mweo!")
    def printName(self):
        print(self.name)
    def __str__(self):
        # return f"{self.name},{self.breed}"
        return f" this method requires name and breed\n method1: print meeooow , \n method 2: print Daniel "
    def trying():
        pass

my_cat = Cat("kitty","persian")
print(my_cat.name)
print(my_cat.breed)  
print(my_cat.meow())
print(my_cat)

# del my_cat.breed
print(my_cat.breed)



class Daniel:
    def __init__(self,name,eyes,nose,ear,tongue,skincolor,limbs,height,):
        self.name = name
        self.eyes = eyes
        self.nose = nose
        self.ear = ear
        self.tongue = tongue
        self.skincolor = skincolor
        self.limbs = limbs
        self.height = height
    def walking(self):
        print("i am walking")
    def talking(self):
        print(" i am speaking")
my_name = Daniel("Daniel",2,2,2,1,"brown","straight",6.1)
print(my_name.ear)
print(my_name.nose)
print(my_name.eyes)
print(my_name.tongue)
print(my_name.skincolor)
print(my_name.limbs)
print(my_name.height)




        
class human:
    def __init__(self,food,sports):
        self.food = food
        self.sports = sports
    def __str__(self):
        return f"cook well for me"
    def walking(self):
        print("i am walking")
    def ThisWillBeAU(self):
        pass 
    def cooking(self):
        print("i am cooking")
his_name = human("sausage","football")
print(his_name.cooking())
print(his_name.walking())
print(his_name.food)
print(his_name.sports)
print(his_name.__str__())

# this is a code that shows games and 

class games:
    def __init__(self,football,basketball,tennis,rugby):
        self.football = football
        self.basketball = basketball
        self.tennis = tennis
        self.rugby = rugby
    def __str__(self):
        return f"i'm playing a game "
SportsMan = games(3,282,4,34)
print(SportsMan.tennis)
print(SportsMan.football)
print(SportsMan.rugby)
print(SportsMan.basketball)
print(SportsMan.__str__())





