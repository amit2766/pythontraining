#! /usr/bin/python3 

import sys

class Array:
    
    def __init__(self, n:int): 
        if type (n) != int:
            raise TypeError ("Size must be integer") 
        self.lst = [] 
        for i in range (n):
            self.lst.append (None) 

    def __len__(self):
        return len (self.lst)

    def __str__(self):
        return (str (self.lst))

    def __getitem__(self, index):
        return (self.lst[index])
    
    def __setitem__(self, index, data): 
        if (index < 0) or (index > (len (self.lst) - 1)):
            raise IndexError ("Array index out of bound") 
        self.lst[index] = data
    
    def __contains__(self, data):
        return (data in self.lst)

    def index_of_element (self, element, start_index=0): 
        if (start_index < 0) or (start_index > len (self.lst) - 1):
            raise IndexError ("Array index out of bound") 
        if element in self.lst[start_index:len (self.lst)]:
            return self.lst.index (element, start_index) 
        else:
            return (-1) 

    def count_of_element (self, element):
        return self.lst.count (element) 

def main ():

    arr1 = Array (10) 
    arr1[0] = 10
    arr1[1] = 20
    arr1[2] = 30  
    arr1[3] = "Hello" 
    arr1[4] = 3.14

    for i in range (len (arr1)):
        print ("arr1[", i, "]:", arr1[i], sep='') 

    lst = [x ** 2 for x in range (10,15)] 
    for i in range (len (lst)):
        arr1[i+5] = lst[i]
    
    for i in range (len (arr1)):
        print ("arr1[", i, "]:", arr1[i], sep='') 

    lst = [1, 243, 346, 1, 457, 34, 1, 243, 5, 10] 
    for i in range (len (lst)):
        arr1[i] = lst[i]

    print (arr1.index_of_element (1))
    print (arr1.index_of_element (1, 1))
    print (arr1.index_of_element (1, 4))
    print (arr1.index_of_element (34, 6))
    print (arr1.count_of_element (1000))
    print (arr1.count_of_element (1))
    print (arr1.count_of_element (34))

    print (len (arr1))
    print (arr1) 
    
    arr2 = Array (5)
    print (arr2) 
    
    if 243 in arr1:
        print ("YES:243") 

    if 1000 in arr1:
        print ("YES:1000")
    else:
        print ("NO:1000")

    try:
        print (arr1[5000])
    except:
        print ("Wrong index 5000") 

    sys.exit (0) 

main () 
