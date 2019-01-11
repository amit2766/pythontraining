def f1(x,y):
    return (x+y)

def f2(x,y,z):
    return (x+y+z)

def f3(x,y,z,w):
    return (x+y+z+w)

class Callable:
    def __init__(self,F):
        self.F=F

    def __call__(self,*args,**kwargs):
        return self.F(*args,**kwargs)


def main():
    c1=Callable(f1)
    c2=Callable(f2)
    c3=Callable(f3)
    print(c1(10,20))
    print(c2(10,20,30))
    print(c3(10,20,30,40))

main()