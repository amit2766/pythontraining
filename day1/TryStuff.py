# L = [True,10,(1,2),"Python"]
# L1 = [True,10,(1,2),"Python"]
# L1 = [True,10,(1,2),"Pythom"]
# print(L)
# print(L1)
import sys

i=10
print(id(i))
i=9
print(id(i))
k=10
print(id(k))
print(sys.getrefcount(i))
