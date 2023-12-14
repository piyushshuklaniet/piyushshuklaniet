def function(n):
 if(n<=363):
    print("No of days does not complete a year")
 elif(n%4==0):
    print("Year is leap year")
 elif(n%400==0):
    print("Year is leap")   
 else:
    print("Year is not leap")
n = int(input("Enter Year"))      
function(n)







def primeinrange(start,end):
    for n in range(start,end+1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                break
        else:
            print(n)

start=int(input("Enter Start:"))
END=int(input("Enter End:"))
primeinrange(start,END)


