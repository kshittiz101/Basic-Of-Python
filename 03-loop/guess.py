# secret="sujan"
# guess=''
# while guess!=secret:
#     guess=input("enter your guess word : ")

# else:
#     print("you won!!")


# secret="sujan"
# guess=''
# count=0
# while count<=5:
#     guess=input("enter your guess word : ")
#     if guess==secret:
#         print("you won")
#         print("do you want to play again?: \n Y for Yes \n N for No")
#         choice=input("enter you choice :")
#         choice=choice.upper()
#         if choice=='Y':
#             continue
#         else:
#             break
#     count+=1

# else:
#     print("Your limit is over!!!")


#check whether given number is prime or not???
a=int(input("enter you number"))
if a>0:
    for i in range(2,a):
        if a%i==0:
            print("this is not prime")
            break
    else:
        print("this is prime")
else:
    print("you shouldnot enter negative value")