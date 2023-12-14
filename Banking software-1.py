name = input("Enter Your Name : ")    
print("Hello",name)

i = int(input("Press 1 to Withdraw Money\nPress 2 to Deposit Money\nPress 3 to know your current balance\nPress 4 to change PIN\n"))

# balance and pin
balance = 1000
pin = 1234

if(i==1):
    withdraw = int(input("Enter amount to withdraw :"))
    if(withdraw>balance):
       print("Insufficient Balance")
    else:
        balance = balance-withdraw
        print("Your updated balance is :",balance)         
if(i==2):
    deposit= int(input("Enter amount to deposit :"))
    balance = balance + deposit
    print("Your amount after deposit is :",balance)
if(i==3):
    pin2 = int(input("Enter your PIN : "))    
    if(pin2==pin):
        print("Your Current balance is : ",balance)
    else:
        print("Incorrect Pin !")     
if(i==4):
        pin3 = int(input("Enter old PIN\n"))
        if(pin3==pin):
            np = input("Enter New PIN :")
            pin=np
            print("Your PIN has been updated successfully updated to - ",pin,"Thank You !")
        else:
            print("Old PIN does not match")
if(i<0):
    print("Enter Valid Input !")
if(i>4):
    print("Enter Valid Input !")