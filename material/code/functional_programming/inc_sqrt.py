#! /usr/bin/python3 

def list_sqrt (L):
    lst = [] 
    for x in L:
        lst.append (x ** 2)
    return (lst) 

def main ():
    L = [x for x in range (5)] 
    L1 = list_sqrt (L) 
    print ("1:L:", L)
    print ("1:L1:", L1)
    
    L2 = list (map ((lambda x : x ** 2), L))
    print ("2:L:", L) 
    print ("2:L2:", L2) 

    L3 = [x ** 2 for x in L]
    print ("3:L:", L) 
    print ("3:L3:", L3)
main () 
