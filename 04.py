#fibonacci function
'''
def fib(n):

 27

8

9

series=[]

10

if n<=0:

 11

 return series

 12

elif:
    (n==1)

    13

    14

series.append(0)

return series

15

else:

16

series=[0,1]

17

18

19

20

21

22

while len(series)<n:

next_num=-series [-1]+series[-2]

series.append(next_num)

return series

n=int(input("Enter a no.:-"))

result=fib(n)

23

print("The fibonacci series is", result)'''


#classwork

'''def ismajors(age):
    if(age>=18):
        return True
    return False
age = [10,12,18,19,21,20,20,18,17,19,23,21,22]
majors=list(filter(ismajors,age))
print(majors)

age = [10,12,18,19,21,20,20,18,17,19,23,21,22]
majors = list(filter(lambda age:age>=18,age))
print(majors)

def isfactor(num):
    if(num%5==0):
     return True
     return False
seq= [1,4,2,5,7,23,45,16,17,27,29]
res = list(filter(isfactor,seq))
print(res)'''

 #map function
 
'''seq= ['1','2','3','4','5','6','7','8','9',]
print("before applying map: ",seq)
res= list(map(int,seq))
print("after applying map",res)

y=mx+c
[1,2,3,4,5]
m=3
c=1
3*x+1


def transformation(x):
   m,c=3,1
   return m*x+c
seq=[1,2,3,4,5,6,2,3,1,5,3,1]
res=list(map(transform,seq))
print(res)

def transformation(x):
   m,c=3,1
   return m*x+c
seq=[1,2,3,4,5,6,2,3,1,5,3,1]
res=list(map(lambda x:3*x+1,seq))
print(res)


from functools import reduce 
seq= [2,5,1,3,7,8,9]
res= reduce(lambda a,b:a+b,seq)
print(res)'''

#Modules and Packages:
'''
'General syntax : from module import function'
if we want to import all the functions from a module we use the following 
syntax : from module import

Other syntax :
  import module
  module.function1(argument)
  module.function2(argument)
  module.function3(argument)
  module.function4(argument)
  module.function5(argument)

  import module as m (this nickmaes the module name to m)
   m.function(arguments)
   m.function(arguments)

(function can also be renamed and used)
from module import function 1 as f1

import module1,module2,module3......
module.function1(argument)
  module.function2(argument),module.function3(argument),module.function4(argument),module.function5(argument),etc...
 '''

import math
print(math.sqrt(25))
'''from math import sqrt
from math import *
import math as m
from math import sqrt as s'''

from math import sqrt 
print(sqrt(49))

import math as m 
print(m.sqrt(43))

from math import sqrt 
print(sqrt(69))

from math import sqrt as s
print(s(49))




