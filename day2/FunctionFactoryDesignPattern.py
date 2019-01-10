def f1(n):
    def f2():
        pass
    def f3():
        pass
    if n is 1:
        return f2()
    else:
        return f3();

# Other example
def GetPowerFunction(iPowerValue):
    def InnerFunction(iBase):
        return (iBase ** iPowerValue)
    return (InnerFunction)

X=GetPowerFunction(2)