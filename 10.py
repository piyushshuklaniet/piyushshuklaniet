#lambda function
'''def doubler(n):
    return n*2
print(doubler(7))'''

'''def tripler(num):
    return num*3
print(tripler(5))'''

'''double=lambda x:x*2
print(double(4),"double of 4")
print(double(int(input("enter a no.:-"))))

lambda_triple=lambda x:x*3
print(lambda_triple(5),"triple of 5")
print(lambda_triple(int(input("enter a no.:-"))))

lambda_sq=lambda x:x*x
print(lambda_sq(4),"sq. of 4")
print(lambda_sq(int(input("enter a no.:-"))))

lambda_even=lambda x:"odd" if x%2 else "even"
print(lambda_even(23))
print(lambda_even(20))
print(lambda_even(int(input("enter a no.:-"))))

lambda_cube=lambda x:x*x*x
print(lambda_cube(4),"cube of 4")
print(lambda_cube(int(input("enter a no.:-"))))

lambda_vote=lambda x:"eligible" if x>=18 else "not eligible"
print(lambda_vote(24))
print(lambda_vote(int(input("enter your age"))))'''

'''map():-
filter():-
reduce():-'''


'''def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))
        
num=int(input("enter num:-",))
print("number:",num)
print('factoral is:',fact(num))

lambda_fact=lambda num: fact(num)
num=int(input("enter a no:-"))
print(lambda_fact(num))

n=int(input("enter a num:="))
i=1
if i in range(1,fact(n+1)):
    i=n*fact(n-1)
    print("fact of",n,"is",i) 
else:
    print("invalid no") '''
    
    
    
#sum of N natural no.
'''def sum_N(start,end):
    if start>end:
        return 0
    else:
        return start+sum_N(start+1,end)
    
start=int(input("Enter starting no.:-"))
end=int(input("Enter endind no.:-"))
result=sum_N(start,end)
print("The sum of Natural no. from",start,"to",end,"is",result)'''


#vote by using lambda function
'''lambda_vote=lambda n:"your are eligible to vote" if n>=18 else "your are note eligible to vote"
print(lambda_vote(int(input("Enter your age:-"))))

#sum of digit of given no
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

#fibonacci function
'''def fib(n):
    series=[]
    if n<=0:
        return series 
    elif n==1:
        series.append(0)
        return series
    else:
        series=[0,1]
        while len(series)<n:
            next_num=series[-1]+series[-2]
            series.append(next_num)
        return series
n=int(input("Enter a no.:-"))
result=fib(n)
print("The fibonacci series is",result)'''

#filter function
'''def isMajor(ages):
    if(ages>=18):
        return True
    return False

ages=[19,20,22,32,45,3]
majors=list(filter(isMajor,ages))
print(majors)

ages=[19,20,22,32,45,3]
majors=list(filter(lambda age:age>=18,ages))
print(majors)

def isfactor(num):
    if(num%5==0):
        return True
    return False
seq=[1,4,2,5,7,23,45,16,13,17,27,29]
res=list(filter(isfactor,seq))
print(res)


seq=[1,4,2,5,7,23,45,16,13,17,27,29]
res=list(filter(lambda num:num%5==0,seq))
print(res)'''

#map function
'''seq=['2','6','8','23','45','67']
print("before applyin map:-",seq)
res=list(map(int,seq))
print("after applying map:-",res)'''

'''def transform(x):
    m,c=3,1
    return m*x+c
seq=[1,2,3,4,5,6,2.3,1.5,3.1]
res=list(map(transform,seq))
print(res)


seq=[1,2,3,4,5,6,2.3,1.5,3.1]
res=list(map(lambda x:3*x+1,seq))
print(res)

n=[1,2,3]
res=list(map(lambda x:x*x*x,n))
print(res)

#reduce function 

from functools import reduce
seq=[2,5,1,3,7,8,9]
res=reduce(lambda a,b:a+b,seq)
print(res)'''


#modules and packages
#A:-module

'''1:-from module import function
                      :-function(arguments)
2:-from module import fun1,fun2,....funN
                      :-fun1(args1),fun2(args2).....funN(argsN)
3:-from module import *
                      :-import all * function
4:-import module
   i.e import modulename.functionname
    import math.pow
5:-import module as m(m is represent module)
                    m.fun1(args1)
                    m.fun2(args2)
6:-from module import function 1 as f1
7:-import module1,module2,module3.......
          module1(f1),module2(f2),module3(f3).....          

import math         
print(math.sqrt(25))
from math import sqrt
print(sqrt(36))
from math import *
print(sqrt(49))
import math as m
print(m.sqrt(9))
from math import sqrt as s
print(s(121))'''

#B:-packages

'''def reminder(divident,divisior):
    return divident%divisor

def division(divident,divisor):
    quotient=divident//divisor
    rem=divident%divisor
    return (quotient,rem)

def cube(n):
    return n**3

def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
        
    return True
def isPythogourus(base,per,hyp):
    if(hyp*2==((base2)+(perp*2))):
        return True
    return Fals'''
    
    
    
#list comprehension

'''cubes=[i**3 for i in range(11)]
print(cubes)
list=[expression for variable in sequence]'''


'''l=[1,2,3,4,5,6,7,8]
l2=[x**2 for x in l if x%2!=0]
print(l2)
 
num=int(input())
factors=[x for x in range(1,num+1) if num%x==0]
print(factors)


def isPrime(n):
    for i in range(2,n//2+1):
        if (n%i==0):
            return False
    return True
    
num=list(map(int,input().split()))
primes=[x for x in num if isPrime(x)]
print(primes)'''






#comprehnsion
'''s={res for res  in [1,2,3] if res%2!=0}
print(s)

s1={s for s in range(20) if s%2==0}
print("set of even:",s1)

s2={n*2 for n in range(20) if n%2}
print(s2)'''

#dict
'''d={101:['Rama',19,500], 102:['Nidhi',20,499], 103:['Anshu',19,500], 104:['Shaily',18,599]}
print(d)
print(type(d))
d1=dict()
print(type(d1))
print(d1)
d1[106]=["shaily",50]
print(d1)
d1[110]=["aryan",18,9.9]
print(d1)'''


#retrieval
'''d={101:['Rama',19,500], 102:['Nidhi',20,499], 103:['Anshu',19,500], 104:['Shaily',18,599]}
print(d)
print(d[101])
print(d.get(101))
#print(d[120])---> key error
print(d.get(120))'''


#verification
'''d={101:['Rama',19,500], 102:['Nidhi',20,499], 103:['Anshu',19,500], 104:['Shaily',18,599]}
print(d)
print("key:",d.keys())
print("values:",d.values())
print("items:",d.items())

for key in d.keys():
    print("keys",key)
    
for value in d.values():
    print("values",value)
for key, values in d.items():
    print(key,"-->",values)
    
d2={105:["nishu",20,454]}
d.update(d2)
print(d)

print("pop:",d.pop(103))
print("popitem:",d.popitem())

sub=['os','c++','c+','java','python']
marks=['40','10']
marks=dict.fromkeys(sub,marks)
print("values of sub:",marks)
'''



#THEORY

      
#map 

'''a=list()
print(a)
b=[10,"Python",42.3,'N',232.63]
print(b)
print(b[3])
n=input().split(',')
print(n)

a=list(map(int,input().split()))
print(a)
b=list(map(float,input().split()))
print(b)'''

#insert,extend,append,extend,

'''b=[10,"Python",42.3,'N',232.63]
print(b)
print(b[3])
b.append("NIET")
print(b)

batch2=["Nidhi","Ananya","shaily"]
batch2.append("peechu")
batch2.append("vidhi")
print(batch2)
batch2.insert(4,"Aryan")
print(batch2)

batch2.append(["Nisha","Rama","pihu"])
print(batch2)
print(batch2[6])
print(batch2[6][0])
print(batch2[6][1])
print(batch2[6][2])

batch2.insert(2,["Kavita","kavya","Dhanvi"])
print(batch2)
a=[1,2,3,4,5,6]
a.append([7,8,9])
print(a)
a.extend([10,11,12])
print(a)'''

#insert,extend,append,extend,pop
'''name=["Nidhi","Ananya","shaily"]
name.insert(0,"prakhar")
name.extend(["piyush"])
name.append(["singh"])

print(name)

print(name.pop())
print(name)
name.pop()
name.pop()
print(name)'''
