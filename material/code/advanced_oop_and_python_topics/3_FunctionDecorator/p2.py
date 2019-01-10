#! /usr/bin/python3 

import sys, time, random

def my_decorator_function (F): 
    line = "-" * 65
    f_handle = open ("arg.log", "w") 
    print (line, file=f_handle) 
    f_handle.close () 
    def wrapper(x, y): 
        f_handle = open ("arg.log", "a") 
        print ("time:", time.ctime (time. time ()), file=f_handle)
        print ("x:", x, "type (x):", type (x), file=f_handle)
        print ("y:", y, "type (y):", type (y), file=f_handle) 
        print (line, file=f_handle) 
        f_handle.close () 
        ret = F (x, y)
        #Epilogue 
        return (ret) 
    return (wrapper) 

@my_decorator_function
def f(n1, n2):
    print ("I am in function f") 
    def g():
        print("I am inside g") 
    return (g) 

def main (): 
    
    for i in range (10):
        my_g = f (random.randint (0, 101), random.randint (101, 201))
        my_g() 
        time.sleep (2) 
    sys.exit (0) 

main () 
