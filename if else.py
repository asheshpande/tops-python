a= int(input("enter value= " ))


if a>0:
    print("A is possitive number ")
else:
    print("A is nagative number ")
    
print("-----------------------------")

if a%2==0:
    print("A is even number")
else:
    print("A is odd number")
    
print("-----------------------------")

a=int(input("enter A: "))
b=int(input("enter B: "))

if a>b:
    print("A is greater number")
else:
    print("B is greater number")

print("-----------------------------")

a=int(input("enter A: "))
b=int(input("enter B: "))
c=int(input("enter C: "))

if a>b:
    if a>c:
        print(" A is greter number")
    else:
        print("C is greter number")
elif b>c:
    print(" B is greter number")
else:
    print("C is greter number")
    
