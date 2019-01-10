#! /usr/bin/python3 

import sys
import random 

def main ():
    lst = [] 
    
    for i in range (10):
        lst.append (random.randint (0,500))

    for x in lst:
        if x % 2 == 0:
            continue
        else:
            print ("x:", x) 

    sys.exit (0) 

main ()
