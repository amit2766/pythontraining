#! /usr/bin/python3 

def gen_squares (N): 
    for i in range (N): 
        yield i ** 2 

def main (): 
    for i in gen_squares (10):
        print ("i:", i, sep='') 
    
    x = gen_squares (10) 
    for j in range (10):
        print (next (x))

main ()
