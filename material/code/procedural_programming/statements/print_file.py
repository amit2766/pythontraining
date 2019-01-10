#! /usr/bin/python3 

import sys

def main (argv): 
    if len (argv) != 2:
        print ("usage error:", argv[0], "file_name")
        sys.exit (-1) 
    f_handle = open (argv[1], "w") 
    
    lst1 = [x for x in range (5)] 
    lst2 = [x for x in range (5,10)] 
    lst3 = [x for x in range (10,15)] 
    lst4 = [x for x in range (15,20)] 

    for i in range (len (lst1)):
        print (lst1[i], lst2[i], lst3[i], lst4[i], 
               sep=':', end='[end]', file=f_handle)
    f_handle.write ("\n") 
    f_handle.close () 
    sys.exit (0) 

main (sys.argv) 

