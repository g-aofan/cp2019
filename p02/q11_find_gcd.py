n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

d = min([n1,n2])

while True:
    if n1 % d == 0 and n2 % d == 0:
        print(d)
        break
    elif d == 0:
        print("Error!")
        break
    d -= 1
    
#alternative solution
#from math import gcd
#print(gcd(30,4))
