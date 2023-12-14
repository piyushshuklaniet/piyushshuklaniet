#remove,clear,pop
'''a=[1,2,3,4,5,6]
a.remove(4)
print(a)
a.remove(6)
print(a)
a.clear()
print(a)'''


'''arr=[1,2,3,4,5,6,7,8,9]
print(arr)
del(arr)
print(arr)'''

#shallow copy
'''a=[1,2,3,4,5,6,7]
b=a
print("a:",a)
print("b:",b)
b[0]=100
print("a:",a)
print("b:",b)'''

#deep copy
'''a=[1,2,3,4,5,6,7]
b=a.copy()
print("a:",a)
print("b:",b)
b[0]=100
print("a:",a)
print("b:",b)

L=[1,2,3,4,5]
for i in range(1,4):
    L[i-2]=L[i]
for i in range(0,4):
    print(L[i],end=" ")'''

#sum function list
'''arr=[1,2,3,4,5,False,0]
print("sum:",sum(arr))
print("max:",max(arr))
print("min:",min(arr))
print("all:",all(arr))  
print("any:",any(arr)) #atleast one value should be none zero
print("len:",len(arr))
print(arr)
print("des.sorted:",sorted(arr))
print(arr)
arr2=list(reversed(arr))
print("reversed:",arr2)
print(arr)
print("aes.sorted:",sorted(arr,reverse=True))'''


#built-in function 
'''print(pow(a,b))  logic:-(a^b)
print(pow(a,b,c)) logic:-(a^b)%c
print(len(123))#error
print(pow(2,3,4,5))#error'''


'''print(len("1234"))                      #4
print(pow(2,2))                         #4
print(pow(8,3,4))                       #0
print(pow(8,4,3))                       #1
print(pow(9,5,5))                       #4
print(max(1,2,3,9))                     #9
print(min(1,3,2))                       #1
print(any([False,False,False,False]))   #False
print(any([0,0,False,True]))            #True'''


'''list()
tuple()
set()
dict()
print()
input()
max():-maximum value from sequence
min():-min. value from sequence
pow():-a^b or (a**b)
len():-gives the lenght startinh with 1
int():- integer
any():-gives True if any input is non zero
all():-gives False if any is input is false'''
#slicing a list 
#used to print spesific range of elements from the list
'''list_name[starting index:ending index:steps]
L[2:]-starting from index 2
l[:5]-print all elements till ending index 4
l[2:6]-print all elements from index 2 till index 5
l[-4:-2]-print all elements from index-4 till index-3
l[0:7:2]-0,2,4,6 index value print 0+2,2+2,4+2
l[7:1:-2]-9,7,5 index value print 7+2 ,5+2,2,3+2
l[-2:-7:-2] -2,-4,-6 index value print -2,-2-2,-4-2,
l[::-1] gives reverse of list from the last index'''

#tuple
'''it is the order collenction of heterogeneous items
it is immutable datatype
its value is not changes 
it use parenthesis "()"
it is statics


1. creation 
t=()---->empty tuple

t1=tuple()
print(t1)---->()empty tuple
 
t2=tuple([1,2,])
print(t2)--->(1,2)

t3=1,2,3,4,5
print(type(t3))--->(1,2,3,4,5)

t4=(1,2,3,4,34.8,'a','niet',[b],(3+8j))
print(t4)--->(1,2,3,4,34.8,'a','niet',[b],(3+8j))


2.addition

3.retrieval

t=(2,5,3,7,8,3,9,10,23)
print(t[0])
print(t[4])
print(t[-3])
print(t[7])
---->2
---->8
---->9
---->10

3.verification
 
4.update

5.delete

6.index

t=(2,5,3,7,8,3,9,10,[2,9],23)
print(t,index(9))--->6 index value of 9 is 6
print(t.count(2))--->1 count only tuple elements inside tuple elements not count in elements are not count
t=(21,51,32,32,51,51,10)
print(t.count(t[t.index(51)+1]))---->2  t[1+1],t[2] 51 comes 1st index'''

#Built in function in tuple
'''sum(t)
max(t)
min(t)
any(t)
all(t)
len(t)'''


'''s={"name":"Piyush","age":"19","salary":"0001","city":"New Delhi"}
value=s.pop('city')
s['location']='Gr.Noida'
print(s)

s={"name":82,"age":65,"salary":75}
minivalue=min(s,key=s.get)
print(minivalue)

s={'emp1':{"name":"Piyush","salary":40000000},'empl2':{"name":"Prakhar Praveen","salary":4000000},'empl3':{"name":"Piyush Maurya","salary":4500000}}
s['empl3']["salary"]=8500
print(s)

s1={10,20,30,40,50}
s2={30,40,50,60,70}
z=s1^s2
print(z)
'''
#slicing
'''string = "we are learning python"
print(string[0:])
print(string[:])
print(string[4:])
print(string[3:15])
print(string[:10])
print(string[::1])
print(string[::2])
print(string[10::2])

print(string[:15:3])


print(string[1:20:4])
print(string[-20:2:2])

print(range([3,10,-1]))

#string is imutable 
string = "Python"

#string[0] = "C"
string = "Cython"
print(string)

import string 
print("ascii_letters:",string.ascii_letters)
print("ascii_lowercase:",string.ascii_lowercase)
print("ascii_Uppercase:",string.ascii_Uppercase)
print("punctuation:",string.punctuation)

print("digits:",string.digits)
print("hexdigits:",string.hexdigits)
print("octdigits:",string.octdigits)
'''
#Homework
''' Q1) Read a list of names of students. Seperate them into list 
         list i) starts with vowels
         list ii) starts with consonants
         list iii) starts with '''


'''s3 = "Python is very easy"
print(s3.replace("e","z"))
print(s3)

s="python is not in cython"
index_i = s.index('i')
print(index_i)
rindex_i = s.rindex('i')
print(rindex_i)

index_n = s.index('n')
print(index_n)
rindex_n = s.rindex('n')
print(rindex_n)
'''
'''s="python is not in cython"
res = s.partition('is')
print(res)

s7="we are in delhi. we are awesome. we are learning python"
cnt = s7.count('w')

cnt2 = s7.count('we')
print(cnt2)

cnt3 = s7.count('in')
print(cnt3)

cnt4 = s7.count('in',1,10)
print(cnt3)'''

'''s= "JhonDipPeta"
mid = len(s)//2
print(len(s),mid)'''

'''def get_middle_three_chars(s):
    if len(s) > 7 and len(s) % 2 != 0:
        middle_index = len(s) // 2
        return s[middle_index - 1 : middle_index + 2]
    else:
        return "Input string should be odd and greater than 7 characters."

# Example usage:
input_string = "abcdefghi"
result = get_middle_three_chars(input_string)
print(result)

def getmiddlethreechars(string):
    mid=len(string)//2
    res= string[mid-1:mid+2]
    return res
string = input("string")
'''
'''passenger_name="Chan"
passpor_name="valid"
if(passport_status=="valid"):
    print("Airport security cleared")
else:
    print("Invalid passport")

islower() returns true if char is uppercase otherwise false'''

'''def getl1st(string):
    lwr=''
    upr=''
    pun=''
    dig=''
    for i in string:
        if i.islower():
            lwr+=i
        elif i.isupper():
            upr+=i
        elif i.isupper():
            dig+=i 
        elif i.isupper():
            pun+=i      
    return lwr+pun+upr+dig
   
string=input()
print(getl1st(string))
'''

def getLowerFirst(string):
    lwr=''
    upr=''
    punc=''
    for ch in string:
        if ch>='a'and ch<='z':
            lwr+=ch
        elif ch>='A' and ch<='Z':
            upr+=ch
        else:
            punc+=ch
    return lwr+punc+upr
string = input()
print(getLowerFirst(string))