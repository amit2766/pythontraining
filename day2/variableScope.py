# print=10 #totally allowed
# print("hello") #TypeError: 'int' object is not callable

# LEGB scope rule: Local, enclosed ,global, builtin

n=10
def f1():

    print("n: ",n) # error UnboundLocalError: local variable 'n' referenced before assignment
    n=11 # this will cause eerror
    print("n: ",n)

# f1()

m=10
def g():
    m=m+1 #error
    print(m)
# g()

o=10
def p():
   global o
   print(o)
   o=12
   print(o)
# p()

#global and nonlocal

def i():
    global o
    o=134
    print (o)
# i()
print(o)

# Only above python 3.6
n=10
print("Start")
def f1():
    n=100
    def f2():
        # print("f2:n: ",n) #Error above python 3.6 below that it was a warning
        # Error was SyntaxError: name 'n' is used prior to global declaration
        global n
        n="hello"
    f2()
f1()


gX1=10
gX2 =20
def thread_entry(x):
    global gX1
    gX2="Hello"

# multi-threading may throw error in above code

def f1():
    n=100 # will not be modified
    def f2():
        n=20 # will be modified
        def f3():
            nonlocal n # modify first occurrence of nonlocal
            print("F3:n: ", n)
        f3()
    f2()
f1()
# if non local is not present then error. If global is not present then it will create a new global.