def IntTwoChecker(F):

    def InnerFunction(x,y):
        if (type(x) is not int):
            raise TypeError("type of first argument must be int")
        if (type(y) is not int):
            raise TypeError("type of second argument must be int")
        return F(x,y)
    return InnerFunction(x,y)

@IntTwoChecker
def Func(x,y):
    return x+y

print(Func(10,11))