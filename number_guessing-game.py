import random as rd
guess=rd.randint(1,20)

user_guess=0
attempt=0

while guess!=user_guess:
 user_guess=int(input("Enetr your guess: "))
 attempt+=1

 if user_guess < 1 or user_guess > 20:
    print("!!!Out of range!!! Please guess between 1 and 20.")
 elif guess>user_guess:
    print("Too low! Try again")
    
 elif guess<user_guess:
    print("Too High! Try again")

 else:
    print("You got it!!")
    print(f"Your total attempt is: {attempt}")

