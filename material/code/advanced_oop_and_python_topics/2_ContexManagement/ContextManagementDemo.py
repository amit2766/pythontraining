class Traceblock: 
    def message(self, msg): 
        print("running:" + msg) 
    def __enter__(self): 
        print("In side __enter__") 
        return self 
    def __exit__(self, exc_type, exc_value, exc_tb): 
        if exc_type is None: 
            print("exiting normally") 
        else: 
            print("type(exc_type):", type(exc_type))
            print("type(exc_value):", type(exc_value)) 
            return True 

with Traceblock() as t1: 
    t1.message("Hello, from t1") 
    print("reached") 

with Traceblock() as t2: 
    t2.message("Constructed t2") 
    try:
        raise TypeError("Dummy type error exception raised") 
    except TypeError: 
        print("Handling exception on my own") 
    print("Not reached") 
