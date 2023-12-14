'''a= list()
print(a)
b=[10,"Python",42.31,'N',253.67]
print(b)

arr = input().split(',')
print(arr)

arr = input().split("@")
print(arr)'''


"""a= list(map(float,input().split()))
print(a)"""

'''dir
   list:
    C- Creation
    A-Adding
      append():-adds value to the last of the list arr.apend
      insert()
      extend()

    R-Retrival

    V-Verification
      in
      not in


    U-Updation
       Updates value at given index 

    D-Deletion
      pop() function removes the last element of list by default and returns it as general output. 
      This function depends on the number of times it is called and removes n times the last element 
      if called n times the last element if called n times. in pop() if we give index in () then that index gets
      deleted and is returnced as output.

      remove(): here, () takes the element as argument which is to be deleted from the list.append

      #note that removes() deletes only first occurance of the argument element, to delete it 
       for 2nd time we need to again the remove() function with same argument.      
    
    C-Clear
      Clear () function removes all elements from the list and leaves the list as empty list.append

      del()
      del() function deletes entire list workspace and even empty list also does is not stored.
      
    
         '''



"""batch1=["Aman,Shivam"]
batch1.append("Prateek")
batch1.append("Saqib")
batch1.append("Saqib")
batch1.append("Nidhi")
print(batch1)"""

"""
arr= [1,2,3,4,5]
arr.append([6,7,8])
print(arr)"""



arr=["Piyush Maurya" , "Prateek" , "Prakhar" ,"Nidhi"]
arr.extend("")
arr.append("ABHISHEK")
arr.pop
print(arr)



l= [1,2,3,4,5]
for i in range(1,4):
    l[i-2] = l[i]

for i in range(0, 4):
    print(l[i],end= " " )

#Implemet the user define fuction to remove multiple values from the set at a given time 


set1={1,2,3,4}
set2={2,4,6,8}
i= set1.intersection(set2)