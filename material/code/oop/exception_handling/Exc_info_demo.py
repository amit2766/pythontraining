import sys

def f1 ():
    raise IndexError("This is deliberate", 10, 3.14, True)

def main ():

    try:
        f1 ()
    except IndexError as I:
    	print ("type(I):", type(I))
    	print(dir(I))
    	print("type(I.args):", type(I.args))
    	for arg in I.args:
            print(arg)
        T = sys.exc_info()
        print ("type (T[0]):", type (T[0]))
        print ("type (T[1]):", type (T[1]))
        print ("type (T[2]):", type (T[2]))
        tb = T[2]
        print("HERE")
        #print(tb.tb_frame.f_lineno)
        #print(exec(tb.tb_frame.f_code))
        print (T[0], T[1], T[2])
        print("END")
        #print(I.with_traceback(T[2]))

main () 
    
