# print((lambda x :x+2) (10))
#
# F = lambda x:x+2
# print (F(12))
#
# # lambda x1,x2,....,xn : R.H.S. (x1,x2,...,xn,v1,v2...,vn,c1,c2,c3..cn) #lambda syntax
#
# a=2
# b=4
# c=6
# lambda x,y,z:a*x**2 +b**y +c**z+10
#
# print("----------------------------------")
# print((lambda n: lambda x:x**n)(2))


######################### MAP ############################

L=[1,2,3,4]
F= lambda x:x**2
M = map(F,L)  # creates object of type map
print(map)
print (" Type of M ", M)   # it is an object
for m in M:
    print (m)
#In a single line
for n in map(lambda x:x**2 ,[n for n in range (1,11)]): print(n)

print("----Nothing will be printed for below expression-----")
for m in M: # nothing was printed because during above loop M was consumed and it was made empty. It is because map itself have __itr__ methods implemented. Hence __next__ method removes the element.
    print (m)
print("-- nothing was printed ---")

# map(func, *iterables) --> map object

#Map takes an object and returns another object

############################### FILTER ####################

# filter(function,iterable)

def F(x):
    return (x%2==0)
L = [1,2,3,4,5,6,7,8,9,10]
X = filter(F,L)
for x in X:
    print (x)

for x in filter((lambda x: x%2==0), [n for n in range(1,11)]) : print(x)

L = [n**2 for n in range(1,11) if n%2==0] # this is comprehension and can be achieved using map and filter
L=list(map(lambda y: y**2,filter(lambda x:x%2==0, range(1,11))))
print(L)

############################## Reduce ############################

from functools import reduce
import operator
print("----------reduce------")
print(reduce (lambda x,y: x+y , [1,2,3,4,5,6]))
print(reduce (operator.add , [1,2,3,4,5,6])) # same as above
print(reduce(lambda x,y:x+y, map(lambda  x:x**2,filter(lambda x:x%2==0, range(1,20)))))

# factorial
print((lambda n:reduce(operator.mul, range(1,n+1))(10)))

print("----------question ------")

print(reduce(lambda x,y:x+y,map(lambda  x:x**2,filter(lambda x:x%2==0, range(1,101)))))
print(reduce(lambda x,y:x*y,map(lambda  x:x**3,filter(lambda x:x%2==1, range(1,26)))))

reduce(lambda x,y:x+y, map(lambda x:x**2, filter(lambda x:x%2==0, range(1,101))))

print(17100*494135778167413574866215164914306640625)
