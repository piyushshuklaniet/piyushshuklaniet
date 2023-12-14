#without comprehension
'''L = [1,2,3,4,5,6,7,8,9]
L2 = []

for i in L:
    if(i%2!=0):
        L2.append(i)
print(L2)

'''
#with comprehsion
'''num=int(input())
factors=[x for x in range (1,num+1) if num%x==0]
print(factors)

nums=list(map(int,input().split()))
primes=[x for x in nums if isprime(x)]
print(primes)'''

'''L=[1,2,3,4,5,6,7,8]
L1=[i for i in L if i%2==0]
print(L1)

print("_data_analytics")

a={1,2,3,4,5,6,7,8,9,10}
b={2,4,6,8,9,3}
print()
'''
'''d2={104:"tommy",105:"jerry",101:"vikky",103:"vikky"}
print(d2)
d3={104:["tommy",5,99],105:["jerry",3],101:["vikky",19,499],103:["vikky",19,49]}
print(d3)
d3[106]=["sharukh",50]
print(d3)
d3[110]=["aryan",18,9.9]
print(d3)
d3[106]=["salman",62]
print(d3)

exp1= 2>1
exp2=4>5
print("exp1 and exp2", exp1 and exp2)
'''
#count until press 0
'''n=int(input())
sum=0
cnt=0
while(n!=0):
    sum+=n
    n=int(input())
    cnt+=1
avg=sum/cnt
print(sum,cnt)
print(avg)'''

#define function

''''def add(a,b):
    result=a+b
    print(result)
       
add(2,5)
add(4,8)'''


'''def product(n1,n2,n3):
    result=n1*n2*n3
    print(result)

product(2,4,6)'''
    
#example with parameter 

'''def product(a,b,c):
    res=a*b*c 
    print(res) 
     
n1=int(input("enter n1:-"))
n2=int(input("enter n2:-"))
n3=int(input("enter n3:-"))
result=product(n1,n2,n3)
print(result)'''

#example wihout parameter

'''def product():
    n1=int(input("enter n1:-"))
    n2=int(input("enter n2:-"))
    n3=int(input("enter n3:-"))
    res=n1*n2*n3 
    print(res) 
     
product()'''


#default arguments

'''def product(a,b,c=1,d=1):
    res=a*b*c*d
    print(res)
result=product(2,3,4)
product(4,6)
product(3,5,7)
product(5,1,2,3)'''

#poitional arguments

'''def product(a,b,c,d):
    print(a,b,c,d)
    res=a*b*c*d
    print(res)
product(2,3,4,5)'''

#keywords argument

'''def student(firstname, lastname):
    print(firstname,lastname)
    
    
student(firstname="nidhi",lastname="singh")
student(lastname="singh",firstname="nidhi")'''

#arbitary arguments length with keywords without order( random output )is dict.

'''def student(**args):
    print(args)  
    for i,j in args.items():
        print(i,":",args[i])
    
student(firstname="nidhi",lastname="singh",age="19",gender="female",branch="aiml")'''


#arbitary arguments length without keywords with  order output is tuple

'''def student(*args):
    print(args)  
    for i in args:
        print(i)
    
student("nidhi","singh","19","female","aiml")'''

#classwork
#define a py. fun. to print all prime no. in a given range


'''def primesinrange(start,end): 
    for i in range(start,end+1):
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                break
        else:
            print(i)
                            
start=int(input("enter a start no."))
end=int(input("enter a end no."))
primesinrange(start,end)'''
    
    
    
    
#python programme to find fact 
  
'''def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))
        
num=int(input("enter num:-",))
print("number:",num)
print('factoral is:',fact(num))

#guru jee
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num=int(input("enter a no.:-"))
print("factorial of",num,"is",fact(num))
fact(num)'''

#sum of no of digits

'''def digitsum(num):
    res=0
    while(num!=0):
        res+=num%10
        num//=10
    return res
num=int(input("enter a number:- "))
print("sum of digits of", num,"is",digitsum(num))


def digitsum(num):
    if(num>0 and num<10):
        return num   
    res=0
    while(num!=0):
        res+=num%10
        num//=10
    return digitsum(res)

num=int(input("enter a number:- "))
print("sum of digits of", num,"is",digitsum(num))'''

#palindrome no.

'''num=int(input("enter a no.:"))
a=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(a==rev):
    print("this no. is palindrome no.")
else:
    print("not a palindrome no.")'''
    
    
#leap year 

'''def year(n):
    if(n%4==0):
        print("year is a leap year")
    else:
        print("year is not leap year")
 
 
  
n=int(input("enter year:-"))
year(n)'''


