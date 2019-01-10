def f1():
    i=10
    print("inside f1 ",i)
    print (p)
    def f2():
        print(locals())
        j=20
        # f1() possible
        print("inside f2 ",i)
    print("f1 again")
    # print(" value of j" ,j) #global name 'j' is not defined error
    f2()

# f1()
#execution of f2() means compilation of body

print(globals()) #prints global symbol table
print(__name__)
print(__doc__)
print(dir(__builtins__)) #prints all builtin variables inside builtin scope
def g():
    print("locals(): ", locals())
    n=10
    print("locals(): ", locals())
    l=[1,2,3]
    print("locals(): ", locals())
# g()


print ("first statament of program")
def f1():
    a=10
    b=20
    c=a+b
    print ("inside f1 c= ", c)
    def f2():
        L=[1,2,3]
        for x in L:
            print ("f2 ",x)
        def f3():
            D={"a":1,"b":2,"c":3,}
            D['d']=100
            for k,v in D.items():
                print ("f3 : ",k,v)
            def f4():
                import math
                print("f4: ", math.sin(math.pi))
            print("in f3 again")
            f4()
            print ("bye f3")
        f3()
    f2()
# f1()
