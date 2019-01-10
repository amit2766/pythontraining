#! /usr/local/bin/python3 

class IntClass:
    def __init__(self, data:int): 
        self.num = data 
    def __add__(self, other): 
        return (self.num + other.num)
    def __str__(self):
        return str (self.num)    
    def __len__ (self): 
        return (100) 
def main (): 
    num1 = IntClass (10) 
    num2 = IntClass (20) 
    print (num1 + num2) 
    print (num1) 
    print (num2)
    print (len (num1))
main ()
