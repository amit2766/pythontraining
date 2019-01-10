#! /usr/bin/python3 

from functools import reduce 

def mul_all (L):
    mul = 1
    for x in L:
        mul = mul * x
    return (mul)

def sum_all (L):
    sum_a = 0 
    for x in L:
        sum_a = sum_a + x
    return (sum_a) 

L1 = [x for x in range (1,6)] 

L_sum_all = reduce ((lambda x, y : x + y), L1)
L_mul_all = reduce ((lambda x, y : x * y), L1)

print ("L_sum_all:", L_sum_all) 
print ("L_mul_all:", L_mul_all) 

x = mul_all (L1) 
y = sum_all (L1) 

print (x, y)
