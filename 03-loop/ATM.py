#ATM in python 
balance=40000
pin_code=1234

print("welcome to Nabil Bank")
print("***********001")
print("processing...")

pin=int(input("enter  your four digit pin code"))

if pin==pin_code:
    while True:
        print('''
          1.Balance Enquiry
          2.Withdraw
          3.Deposite
          4.Exit
        ''')

        choice=input("please select a valid option : ")
        if choice=='1':
            print(f"Your total balance is {balance}")
            break
        elif choice=='2':
            withdraw_amt=int(input("enter your amount : "))
            balance-=withdraw_amt

            print(f"{withdraw_amt} is debit from your account")
            print(f"Your total balance {balance}")
            break

        elif choice=='3':
            deposite_amt=int(input("enter your deposite amount : "))
            balance +=deposite_amt
            print(f"{deposite_amt} creadit in you account")
            print(f"Total balance is {balance}")
            break   
        elif choice=='4':
            print("Thanks for visiting!!!")
            break
        else:
            print("invalid ,keyword!!!")

else:
    print("please enter a valid number !!!!")