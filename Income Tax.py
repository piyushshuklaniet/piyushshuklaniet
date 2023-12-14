#Calculate the income tax 

n=int(input("Employee Income :"))


if(n<10000):
    
        print("Yours Employee Salary comes under Zero Tax slab")

else:
        a=n-10000
        b=a-10000
        c=n-20000

        Tax1=a*0
        Tax2=b*0.1
        Tax3=c*0.2

Totaltax=Tax1+Tax2+Tax3

print("Your total tax is ",Totaltax)

