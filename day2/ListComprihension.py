A=[1,2,3,4,5]

# L=[<v> for <v> in <iterator>] #Version 1
L=[n for n in range(1,20)]
print(L)
L=[n for n in "Hello world"] #with filter condition
print(L)
L=[n**2 for n in range(1,5)]
print(L)

# L=[<v> for <v> in <iterator> if conf(v)] #Version 2 #with filter condition
L=[n for n in range(1,20) if n%2==0]
print(L)

import math
def isPrime(x):
    if (x==2 or x==1):
        return False
    for i in range (2,math.floor(math.sqrt(x))+1):
        if(x%i) == 0:
            return False
    return True
L=[n**2 for n in range (1,100) if isPrime(n)]
print("Prime ", L)

f=open("/Users/amit/projects/python/pythontraining/day2/somefile","r")
print(f.readline())

L= [(a,b) for a in range(1,5) for b in range (5,7)] #cartesian product
print(L)
L= [a+b for a in range(1,5) for b in range (5,7)]
print(L)
L= [a+b for a in range(1,5) if a%2==0 for b in range (5,7)]
print(L)
L= [a**2+b**2 for a in range(1,15) if a%2==0 for b in range (5,10) if b%2==1]
print(L)