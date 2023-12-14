#Shoppig Price App
MP = int(input("Enter the Marked Price \n"))

if(MP>10000):
    Sp=MP-(20/100)*MP
    print(Sp, "is the selling price")
if(7000<MP<=10000):
    Sp=MP-(15/100)*MP
    print(Sp, "is the selling price")
if(MP<=7000):
    Sp=MP-(10/100)*MP
    print(Sp, "is the selling price")
