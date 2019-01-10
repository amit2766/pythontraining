class T1:
    pass 

class TraceBlock:
    def message(self, arg):
	    print('running ' + arg)
    def __enter__(self):
	    print('starting with block')
	    return self
    def __exit__(self, exc_type, exc_value, exc_tb):
	    if exc_type is None:
                print('exited normally\n')
            else:
                print('__exit__:raise an exception! ' + str(exc_type))
                print("__exit__:exc_value:", exc_value) 
                return False   #Propagate

with TraceBlock() as action:
	action.message('test 1')
	print('reached')

with TraceBlock() as action:
	action.message('test 2')
	raise TypeError("HAHHAHAHHAHHAHHA") 
	print('not reached') 
