# fizzbuzz
"""
fizzbuzz

you are to build a program that will print out from numbers 1 to 30

now while it prints this out,once it gets to the number 3 or any number divisible by 3 it should print out the word ”fizz” 

if it gets to a number 5 or divisible by 5 it should print out the word “buzz”   """

begin = 1 
end = 30 
while(begin < end ):
    
    print(f"This is the value starting point  {begin}")
    begin = begin + 1 
    if begin % 3 == 0:
        print(f"{begin}fizz")
    elif begin % 5 == 0:
        print(f"{begin}buzz")

    print(begin)