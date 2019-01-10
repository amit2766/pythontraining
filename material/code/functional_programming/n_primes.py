#! /usr/bin/python3 

import sys
import math

def is_prime (p):
    n = math.floor (math.sqrt (p))
    for i in range (1, n+1):
        if p % i == 0 :
            if i != 1 and i != p:
                return False
    return (True)

def main ():
    L = [x for x in range (100) if is_prime (x) == True]
    print (L) 
    
    L1 = list (filter (is_prime, [x for x in range (100)]))
    print (L1) 

    L2 = [(x, y) for x in range (100) 
                for y in range (100) if x + y == 50]
    print (L2)   
    sys.exit (0)

    

main ()
