#! /usr/bin/python3 

import sys

class StudentRecord: 
    def __init__(self, e_name, e_id, e_sal):
        self.name = e_name
        self.eid  = e_id
        self.sal  = e_sal 
    def get_name (self):
        return self.name
    def get_id (self):
        return self.eid
    def get_sal (self):
        return self.sal
    def set_name (self, e_name):
        self.name = e_name
    def set_id (self, e_id):
        self.eid = e_id 
    def set_sal (self, e_sal):
        self.sal = e_sal 

def main ():
    print ("Enter name:", end='')
    e_name = input ()
    print ("Enter id:", end='')
    e_id = int (input ())
    print ("Enter sal:", end='')
    e_sal = float (input ())
    st1 = StudentRecord (e_name, e_id, e_sal) 
    print (st1.get_name (), st1.get_id (), st1.get_sal ()) 
    sys.exit (0) 

main () 

