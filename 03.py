'''num=int(input("Enter the number :"))

for i in range(2, int(num**0.5)+1):

    if(num%i==0):
        print("not prime")

        break
else:
    print("prime")


def add(a,b):

    result=a+b
    print(result)


add(2,5)

add(4,8)

def product(a,b,c):

      res = a*b*c
      print(res)  


a = int(input("Enter n1: "))

b= int(input("Enter n2: "))

c = int(input("Enter n3: "))
product(a,b,c)

def student(firstname,lastname):
    print(firstname,lastname)

student(lastname="Shukla",firstname="Piyush")


#VARIABLE LENGTH KEYWORD ARGUMENT

def student(**args):

    for  i,j in args.items():

        print(i,":",args[i])

student(firstname="Piyush" ,middlename="Kumar",lastname="Shukla",age="19",DOB="25/03/2004")



def primesinranger(start,end):

    for n in range(start,end):

        for i in range(2,int(n**0.5)+1):


def factorial(num):

    factorial = 1

    for i in range(1,num+1):

        factorial *=i
    return factorial

num= int(input("Enter a number: "))

print()

def factorial(number):
    if(number==0 or number==1):
        return 1
    return number*factorial(number-1)

number = int(input("Enter a number"))
print(factorial(number))


def digitsum(number):
    res=0
    while(number!=0):
        res += number%10
        number//= 10
    return res
number = int(input("Enter a number : "))
print("sum of digits of ", number,"is",digitsum(number))

print(pow(8,4,4))

print(pow(1,5,8))

print(input("Hello the numnber of the system : "))


print(max(1,2,3,4,9,5,8,7,2,1,4,5,2,3,0,5,4))

print(any[0,0,7])

lambda_doubler = lambda x:x*2
print(lambda_doubler(8))

lambda_squarer = lambda x:x*x
print(lambda_squarer(5))'''


'''lambda_even = lambda x: "odd" if x%2 else "even"
print(lambda_even(23))

lambda_odd = lambda x: "even" if x%2 else "odd"
print(lambda_odd(26))

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")'''

def sum_n(start,end):
    if start>end:
        return 0
    else:
        return start+sum_n(start+1,end)
        
start=int(input("enter starting no:-"))
end=int(input("enter ending no:-"))
result=sum_n(start,end)
print("the sum of Natural no from",start,"to",end,"is",result)




