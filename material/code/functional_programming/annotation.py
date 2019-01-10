#! /usr/bin/python3 

def intersect (X:list, Y:list)->list:
    res = []
    if ((type (X) != list)):
        raise TypeError ("X is expected to be of type:", 
                          intersect.__annotations__['X'], 
                          "but X is of the type", type (X))
    if (type (Y) != list):
        raise TypeError ("X is expected to be of type:", 
                          intersect.__annotations__['Y'], 
                          "but Y is of the type:", type (Y))
    for x in X:
        if x in Y:
            res.append (x)
    if type (res) != list:
        raise TypeError ("res is expected of the type:",
                          intersect.__annotations__['res'], 
                          "but res is of the type:", 
                          type (res))
    return (res)

L = intersect ([1,2,3,4,5], [3,4,5,6,7,8])
print (L) 
L = intersect ({1,2,3,4,5,6}, {3,4,5,6,7,8})
print (L) 
