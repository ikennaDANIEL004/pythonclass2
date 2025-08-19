#Assignment 1(Directions from aptech to emene and aptech to Abakpa )
my_name = input("What is Your Name?   ")
Direction = input("Enter your Location (Abakpa or Emene)  ").lower()

if Direction == "emene":
    print(f"{my_name} this is the Direction to {Direction} ")
    print("Head east from aptech to holyghost\n From holyghost to old park bus stop \n Head to port-Harcourt express \n Countinue for about 5-7 km, passing artisan market \n look for signs for Emene \n Turn left onto the Nike lake- Harmony Estate -Emene \n You will arive in Emene, near land marks like the Eke- Obinagu Junction ")
    print("YOU  HAVE ARRIVVED EMENE")
elif Direction == "abakpa":
     print(f"{my_name} this is the Direction to {Direction} ")
     print("To get to Abakpa From Aptech \n You Have to head west from Aptech to P & T leading to ogui Junction \n move straight to Abakpa Junction very close to 82 Division  \n Move left to onitsha expressway then move straight then tilt left  ")
     print(f" You have reached your Destination {Direction}")

else:
     print(f"invalid Destination: {Direction} is not an option ")