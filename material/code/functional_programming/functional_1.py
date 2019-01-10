#! /usr/bin/python3 

from functools import reduce 
import operator 

L = list (range (-5, 5))
print (L) 

L1 = list (filter ((lambda x : x > 0), range (-5,5)))
print (L1)

def pos (L):
    res = [] 
    for x in L:
        if x > 0:
            res.append (x) 
    return (res)

print (pos (list (range (-5,5))))

print (reduce ((lambda x, y : x + y), [1,2,3,4]))
print (reduce ((lambda x, y : x * y), [1,2,3,4,5]))
print (reduce (operator.add, [1,2,3,4]))
print (reduce (operator.mul, [1,2,3,4]))
