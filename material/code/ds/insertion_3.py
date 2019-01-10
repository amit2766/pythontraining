#! /usr/bin/python3 

import sys
import random 
import time 

def input_list (n):
    random.seed (int (time.time ()))
    lst = [] 
    for i in range (n):
        lst.append (random.randint (0, 10*n))
    return (lst) 

def output_list (lst): 
    for i in range (len (lst)):
        print ("lst[", i, "]:", lst[i], sep='') 

def sort_list (lst):
    for j in range (1, len (lst)):
        key = lst [j]
        i = j - 1
        while i > -1 and lst[i] > key:
            lst[i+1] = lst[i] 
            i = i - 1
        lst[i+1] = key 

def main (argv):
    if len (argv) != 2: 
        print ("usage error:", argv[0], "n") 
        sys.exit (-1) 
    n = int (argv[1])
    lst = input_list (n)
    sort_list (lst)
    output_list (lst)
    sys.exit (0) 


main (sys.argv) 
