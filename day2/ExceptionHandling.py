"""try:
    Block       #syntax one
except:
    Block"""

"""
try:
    Block   #syntax 2
except TypeError:
    Block
except:
    Block"""

# RecursionError can also be handled in Python.

"""
try:
    Block   #syntax 3
except TypeError:
    Block
except:
    Block
finally:
    Block

"""

"""
try:
    Block   #syntax 4 #### ELSE BLOCK with try catch
except TypeError as t:
    Block
except ValueError, OtherError as e:
    Block
except:
    Block
else:
    ELSE BLOCK
finally:
    Block

"""

try:
    print("try")
except:
    print("except")
else:
    print("else")
finally:
    print ("finally")



n = 5
assert n>0 , "N must be positive" # just like junit assert

try:
	n=-10
	assert n>0, "n must be positive"
except:
	print("Except is here")
