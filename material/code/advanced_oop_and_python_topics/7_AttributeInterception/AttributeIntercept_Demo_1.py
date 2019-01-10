#def __getattr__(self, name):		# On undefined attribute fetch [obj.name]
#def __getattribute__(self, name):	# On all attribute fetch [obj.name]
#def __setattr__(self, name, value):# On all attribute assignment [obj.name=value]
#def __delattr__(self, name):		# On all attribute deletion [del obj.name]

class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
        print ("Get:type (name):", type (name))
        #raise NotImplementedError("Object of type", type(self), "does not contain attribute", name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))
        print ("Set:type (name):", type (name))
        print ("Set:type (value):", type (value))

X = Catcher () 
X.job 
X.pay 
X.pay = 99 
print("X.pay", X.pay)
