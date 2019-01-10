def f1():
    def f2(X):
        print ("X: ",X)
    return (f2)
Y=f1()

print ("Type Y : ",type(Y))

Y(10)
f1()(10) #same as above statement

def f1():
    x=100
    def f2():
        print ("X ",x)
    return (f2)
Y=f1()
Y() # will print 100. Even before f2 is called f2 will save state of f1. Implicit state saving. F2 will save only variables used within F2 by F1.

