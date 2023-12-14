# GREATEST NUMBER AMONG 3 DISTINCT NUMBERS
a = int(input("Enter number A :\n"))
b = int(input("Enter number B :\n"))
c = int(input("Enter number C :\n"))

if(a>b):
    if(a>c):
        print(a," is greatest")
    if(a<c):
        print(c," is greatest")
if(c>a):
    if(c>b):
        print(c," is greatest")
    if(c<b):
        print(b," is the greatest")


#Home work
'''
Q1 filter the worlds of length more than 3 from given sequence of word by using lambda funtion
Q2 map the given to cubic transofmation by using lambda function 
Q3 calculate sum of squares of the given values of the given data using reduce functions''' 
