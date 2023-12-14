#File Handling
'''open
read/write
close'''

'''opening:
       open("absolute path of the file",'mode')
note that if the file is in given else we give absolute path 

there are three modes :-
r- read
w-write 
a-append'''

#dict comprehnsion
'''d={key:key**2 for key in range (10) if key%2}
print(d)'''

#nested dict
'''d={1:{'a':10,'b':20},2:{'x':100,'y':200}}
print(d)
print(d[1])
print(d[1]['b'])
#access
print(d[2]['y'])
#add
d[1]['b']=20
print(d)
#update
d[1].update({'c':30,'d':40})
print(d)'''


'''n_list=[[3,9],[2,5],[1,7],[4,2]]
sorted_l=sorted(n_list,key=lambda x:x[1])
print(sorted_l)'''

'''import math
list1=input("Enter your list:").split(",")
sorted_l=sorted(list1)
sumthree=sum(sorted_l[:3])
print(sumthree)'''




#string
'''st="we are learning python"
print(st)
print(type(st))
#forward string
print(st[0])
print(st[3])
print(st[7])
print(st[20])
#print(st[24]) index error out of range
#backward string
st="we are learning python"
print(st[-1])
print(st[-10])
print(st[-16])#space
print(st[-22])
#slicing
st="we are learning python"
print(st[0:])
print(st[:])
print(st[4:])
print(st[3:15])
print(st[:10])
print(st[::1])
print(st[::2])
print(st[10::2])
print(st[:15:3])

print(st[-5:])
print(st[-20:-5])
print(st[:-15])
print(st[:-10:1])
print(st[::-1])#---->reverse of the string
print(st[::-3])
print(st[1:20:4])
print(st[-20:-2:2])
print(st[:5:-1])
print(st[5:2:])#---->give none'''


'''def palindrome(num):
    numstr=str(num)
    reverstr=numstr[::1]
    return numstr==reverstr
    
num=int(input("Enter your no."))
w
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")

for i in range(3,10,-1):
    print(i)


# string is immutable 
#constant data type cannot be change for immutable sequence we cannot change single element seq. but we can reintalise with other type of seq
st='python'
st='cython'
print(st)


import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print("punctuation:",string.punctuation)
print("digit:",string.digits)
print("hexadigit:",string.hexdigits)
print("octadigit:",string.octdigits)


s1='python'
print(s1.endswith('n'))
print(s1.endswith('ython'))
print(s1.endswith('m'))

s2='Cythpn'
print(s2.startswith('C'))
print(s2.startswith('Cyt'))
print(s2.startswith('c'))'''


#vowelnames
'''names=input().split()
vowelnames=[]
consnames=[]
for name in names:
    if name[0] in "aeiouAEIOU":
        vowelnames.append(name)
    else:
        consnames.append(name)
        
print("list-i:",vowelnames)
print("list-ii:",consnames)'''

'''s3='Python is very easy'
print("s3",s3)
print("after changing:",s3.replace('e','Z'))  # new copy of the result
print('s3',s3.replace('is','was'))
print("s31",s3.replace('easy','hard'))
s4='12345'
print("s4",s4.isdigit())
s5='123a'
print("s5",s5.isdigit())
print("s5",s5.isdecimal())
print("s4",s4.isdecimal())

s6='abc'
s7='abc5'
s8='Sky Is The limit'
print('s6',s6.isalpha())
print('s7',s7.isalnum())
#print('s8',s8.isnum())



s="Python is not Cython"
us=s.upper()
ls=s.lower()
scs=s.swapcase()
ts=s.title()
print("string:",s)
print("upper:",us)
print("lower:",ls)
print("swapcase:",scs)
print("title",ts)

s='Python is not in Cython'
index_i=s.index('i')
rindex_i=s.rindex('n')
print("index",index_i)
print("rindex",index_i)'''



sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

max_value = max(sample_dict.values())

for key, value in sample_dict.items():
    if value == max_value:
        print(key)
