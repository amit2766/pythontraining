class StudentRecord: 
    def __init__(self, name, roll, city): 
        if type (name) != str or type (roll) != int or type (city) != str: 
               raise TypeError ("Bad argument") 
        self.st_name = name 
        self.st_roll = roll 
        self.st_city = city 

    def get_name (self): 
        return (self.st_name) 

    def get_roll (self): 
        return (self.st_roll) 

    def get_city (self): 
        return (self.st_city) 

    def set_name (self, new_name): 

        if type (new_name) != str: 
            raise TypeError ("Bad argument") 

        self.st_name = new_name 

    def set_roll (self, new_roll): 

        if type (new_roll) != int: 
            raise TypeError ("Bad argument") 

        self.st_roll = new_roll 

    def set_city (self, new_city): 

        if type (new_city) != str: 
            raise TypeError ("Bad argument") 

        self.st_city = new_city 
    
    def dump (self): 
        print ("Name:", self.st_name)
        print ("Roll:", self.st_roll)
        print ("City:", self.st_city) 

