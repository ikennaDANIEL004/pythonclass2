""""
Guess the Number:
Set a secret number (e.g., 7) and Ask the user to guess the number.
Keep asking until they guess correctly
When guessed right, print "Correct! You win."
"""

def number():
    secret_number = 7
    ask = int(input("Guess the secret number   "))
    while ask != secret_number:
        print("try again")
        ask = int(input("Guess the secret number   "))
    else:
        print("correct you win!")

number()
