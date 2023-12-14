'''status="morning"
if(status=="morning"):
    print("It is Morning")
    print("We can have breakfast")
print("We are in NIET")
print("We are Engineers !")   

status="afternoon"
if(status=="afternoon"):
    print("It is afternoon")
    print("We can have Lunch")
print("We are in NIET")
print("We are Engineers !")  

status="Evening"
if(status=="Evening"):
    print("It is Evening")
    print("We can have Supper")
print("We are in NIET")
print("We are Engineers !")  

status="Night"
if(status=="Night"):
    print("It is Night")
    print("We can have Dinner")
print("We are in NIET")
print("We are Engineers !")

day="tuesday"
if(day=="sunday"):
    print("Holiday")
else:
    print("working day")

day="second saturday day"
if(day=="sunday"):
    print("Holiday")
else:
    print("working day")

number=25
if(number>0): 
    if(number%5==0):
        print("My Favourite")
    else:
            print("Your Favourite")
else:
    print("My Favourite")

number=-5
if(number>0): 
    if(number%3==0):
        print("My Favourite")
    else:
            print("Your Favourite")
else:
    print("Not Favourite")

number=52
if(number>0):
    print("Positive")
elif(number<0):
        print("Negative")
else:
    print("Zero")
    
number=11
if(number>0): 
    if(number%3==0 and number%7==0):
        print("Our Favourite")
    elif(number%3==0):
        print("My Favourite")
    elif(number%7==0):
        print("Your Favourite")
    else:
        print("Not favourite")

number=int(input("Enter a number:"))
if(number%3==0 and number%7==0):
   print("Our Favourite")
elif(number%7==0):
    print("Your Favourite")
elif(number%3==0):
    print("My Favourite")
else:
    print("Not Favourite")


for val in range(15):
    print(val)

for char in "NIET":
    print(char)

for val in {1,2,3,5,8,4}:
    print(val)


start= int(input("Enter start range"))
END=int(input("Enter end range"))
for number in range(start,END):
    if(number%3==0 and number%7==0):
       print(number)



for i in range(10):
    if(i==3):
        print(i+2)
        i+=4
    else:
        print(i)

for i in range(15):
    if(i==5):
        print(i+5)
    else:
        print(i-1)


for i in range(10):
    for j in range(1,10):
        if(i%j==0):
           print(i*j)
        else:
            print(i+j)

 
number=int(input())
k=1
while(number>0):
    print(number)
    number-=k
    k+=2

n=1
while(n<10):
    if(n==4):
        print(n-5)
    else:
        print(n+2)
    n+=2

number=15
while(number<25):
    i=1
    while(number%i==0):
        print(number,i)
        i+=2
    number+=5

for i in range(10):
    if(i==3):
        continue 
    print(i)
else:
        print(i)
i+=1

i=1
while(i<10):
    if(i%2==0):
        i+=1
        continue
        print(i)
    else:
        print(i)
        i+=1
 
for i in range(8):
    if(i==4):
        break
    print(i)
else:
   print(i)


for i in range(10):
    print(i)
    pass
print(i+1)'''



number=int(input("Enter a number:"))
if(number%3==0 and number%7==0):
   print("Our Favourite")
elif(number%7==0):
    print("Your Favourite")
elif(number%3==0):
    print("My Favourite")
else:
    print("Not Favourite")


