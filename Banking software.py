Name = input(("Name of the Client: \n"))
("\n")
print("Hello",Name)
#balance and pin
#amount
#money

balance=1000
balance1=10000

pin=7438
Currentpin=2016

i = int(input("Press 1 to Withdraw Money\nPress 2 to Deposit Money\nPress 3 to know your current balance\nPress 4 to change PIN\n"))
if(i>4 or i<0):
    print("Invalid Attempt")
else:
    if(i==1):
      pin2=int(input("Enter the PIN : "))
      if(pin2==pin):
        withdraw = int(input("Enter the amount to Withdraw : "))
        if(withdraw>balance):
         print("Amount asked for Withdrawl is more than current saving's balance")
        else:
            balance=balance-withdraw
            print("Your account is debited by ",withdraw)

            print("Your updated Account balance is ",balance)
      else: 
        print("Wrong PIN mentioned!!!")
    if(i==2):
     deposit=int(input("Enter the amount to Deposit : "))
     balance=balance+deposit 
     print("Your account is credited by ",deposit)
     print("Your New account balance is ",balance)
    if(i==3):
     pin3=int(input("Enter the PIN: "))
     if(pin3!=Currentpin):
             print("Wrong Pin mentioned") 
     else:
           (pin3==Currentpin)
     currentwithdraw=int(input("Enter the amount to withdraw: "))
     balance2=balance1-currentwithdraw
     print("Your account is debited by ",currentwithdraw)
     print("Your Current Account Balance is ",balance2)
    if(i==4):
        pin3 = int(input("Enter old PIN\n"))
        if(pin3==pin):
            np = input("Enter New PIN :")
            pin=np
            print("Your PIN is succesfully changed to",pin,"Thank You !")
        else:
            print("Old PIN does not match")
 
 #end
 