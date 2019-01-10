def f1(): 
    f2() 

def f2():
    f3() 

def f3(): 
    raise TypeError("Test exception") 

f1() 
