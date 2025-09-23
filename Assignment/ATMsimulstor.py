"""
[9/7/2025 4:31 AM] +234 912 861 8084: For the second assignment
A Simple ATM Simulator

Start with a balance of $1000
Ask user what they want to do: check balance, deposit, or withdraw
For deposits: add amount to balance
For withdrawals: check if sufficient funds exist
Display appropriate messages and updated balance
[9/7/2025 4:32 AM] +234 912 861 8084: for this one
it will also be a console app
just like everything else
the atm simulator should look something like this
ATM Menu:
1. Check Balance
2. Deposit
3. Withdraw
Choose an option: 3
Enter withdrawal amount: $150
Transaction successful! New balance: $850
"""
import time
print("welcome to my ATM simulator ")
balance = 1000
print ("1. Check balance \n 2.  Deposit \n 3. Withdraw")
choose = input("choose an option:  ")
if choose == "1":
    print(f"your balance is ${balance}")
elif choose == "2":
    deposit = int(input("enter deposit amount:  "))
    new_balance = int(balance + deposit)
    print(f"your new balance is ${new_balance}")
elif choose == "3":
    withdraw = int(input("How much do you want to withdraw  "))
    if withdraw > balance:
        print("withdrawal processing ")
        time.sleep(10)
        print("insufficeint fund 😒")
    
        
    else:
        print("withdrawal processing ")
        time.sleep(10)
        print(f"your about to withdraw ${withdraw}")
        print("Withdrawal successful ")
        print(f"your balance is ${balance - withdraw}")
        


        

    

    
