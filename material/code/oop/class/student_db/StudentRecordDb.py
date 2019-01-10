import StudentRecord

class StudentRecordDb: 
    
    def __init__(self): 
        self.st_lst = [] 

    def add (self, st_rec): 

        if type (st_rec) != StudentRecord.StudentRecord: 
            raise TypeError ("Bad argument") 

        self.st_lst.append (st_rec) 


    def delete (self, roll): 
        
        if type (roll) != int: 
            raise TypeError ("Bad argument") 

        for i in range (len (self.st_lst)):
            if roll == self.st_lst[i].get_roll (): 
                break
        else: 
            raise ValueError ("Roll number not found") 

        del (self.st_lst[i]) 

    def search (self, roll): 
        
        if type (roll) != int: 
            raise TypeError ("Bad argument")

        for record in self.st_lst: 
            if roll == record.get_roll (): 
                return (record) 

        return None 
    
    def edit (self, roll): 

        if type (roll) != int: 
            raise TypeError ("Bad argument") 

        for record in self.st_lst: 
            if roll == record.get_roll (): 
                break 
        else: 
            raise ValueError ("Bad roll number") 

        ans = input ("Do you want to modify name? :") 
        if ans == "y" or ans == "Y": 
            new_name = input ("Enter new name:") 
            record.set_name (new_name) 

        ans = input ("Do you want to modify city? :") 
        if ans == 'y' or ans == 'Y': 
            new_city = input ("Enter new city:") 
            record.set_city (new_city) 
    
        print ("Record has been updated to:") 
        print ("Name:", record.get_name ()) 
        print ("Roll:", record.get_roll ()) 
        print ("City:", record.get_city ()) 

    def dump_all (self): 
        line = "-" * 75 
        print (line) 
        for record in self.st_lst:
            record.dump () 
            print (line) 
