#! /usr/bin/python3 

import sys

def add_ten (L):
    for i in range (len (L)):
        L[i] += 10

def main ():
    L = [x for x in range (10)] 
    print ("Original L:", L) 
    add_ten (L) 
    print ("After, add_ten (L):", L) 

    L1 = [x for x in range (20, 30)]
    print ("Original L1:", L1) 
    L1 = list (map ((lambda x : x + 10), L1))
    print ("After L1 = list (map ((lambda x : x + 10), L1)), L1:", L1)
    
    print ("Multiply every element in L1 by 10") 
    print (list (map ((lambda x : x * 10), L1)))

    sys.exit (0) 

main ()
   
