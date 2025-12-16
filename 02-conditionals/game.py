#game 
a="welcome to our game"
print(a.center(70,"-"))
print("S for Sissor P for Papper R for Rock")
print("remember!!! S>P , P>R R>S")

user=input("enter your choice : ")
user=user.upper()

import random
computer=random.choice(['S','P','R'])

print(f" You choose a : {user}")
print(f"computer choose :{computer}")

if (user=='S' and computer=='P') or (user=='P' and computer=='R') or\
    (user=='R' and computer=='S'):
    print("You won!!!")

elif user==computer:
    print("draw!!!")
elif user not in ['S','P','R']:
    print("please enter valid keyword!!!!")
else:
    print("computer won!!!")

