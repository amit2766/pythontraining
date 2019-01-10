# First format 
try: 
	st1
	st2
	st3
except <Name>: 
	st1
	st2
	etc
# ----------------------------
# Second format 
try: 
	st1
	st2
	st3
except <Name1>: 
	st1
	st2
	etc
except <Name2>: 
	st1
	st2
	etc
except: 
	st1
	st2
	etc
#-----------------------------
# Third format 
try: 
	st1
	st2
	etc
except <Name1>: 
	st1
	st2
	etc
except <Name2> as V1: 
	st1
	st2
	etc
except <Name1, Name2>: # Name1 or Name2, come here
	st1
	st2
	etc
except <Name1, Name2> as V2: # Name1 or Name2
	st1
	st2
	etc
except: 
	st1
	st2
	st3
#---------------------------------------
#Fourth format 
try: 
	st1
	st2
	etc
except <Name1>: 
	st1
	st2
	etc
except <Name2> as V1: 
	st1
	st2
	etc
except <Name1, Name2>: # Name1 or Name2, come here
	st1
	st2
	etc
except <Name1, Name2> as V2: # Name1 or Name2
	st1
	st2
	etc
except: 
	st1
	st2
	st3
else: 	# If no exception is raised in try block then come here  
	st1
	st2
	etc
#--------------------------------------
# Fifth format 
try:
	st1
	st2
	etc
finally: # Always run this code way out 
	st1
	st2
	etc
#-------------------------------------------
# Sixth format 
try:
	st1
	st2
	etc
except <Name1>: 
	st1
	st2
	etc
except <Name2> as V1: 
	st1
	st2
	etc
except <Name1, Name2>: # Name1 or Name2, come here
	st1
	st2
	etc
except <Name1, Name2> as V2: # Name1 or Name2
	st1
	st2
	etc
except: 
	st1
	st2
	st3
finally:  # always come here, with or without exception 
	st1
	st2
	etc
#----------------------------------------------------------
# Seventh form : Most general, unified try/except/else/finally 
try:
	st1
	st2
	etc
except <Name1>: 
	st1
	st2
	etc
except <Name2> as V1: 
	st1
	st2
	etc
except <Name1, Name2>: # Name1 or Name2, come here
	st1
	st2
	etc
except <Name1, Name2> as V2: # Name1 or Name2
	st1
	st2
	etc
except: 
	st1
	st2
	st3
else:
	st1
	st2
	st3
finally:  # always come here, with or without exception 
	st1
	st2
	etc
#-----------------------------------------------------
# Except can be written in follwing ways 
#[1]
except <Name1>: 
	st1
	st2
	etc
#[2]
except <Name> as V: 
	st1
	st2
	etc
#[3]
except <Name1, Name2, ...>: 
	st1
	st2
	etc
#[4] 
except <Name1, Name2, ...> as V: 
	st1
	st2
	etc
#[5] 
except: 
	st1
	st2
	st3
	etc
#----------------------------------------------------
# Raise can be written in following ways 
raise <Instance>  # Raise instance of a class
raise <Class> 	  # Raise class	
raise 			  # Raise last exception 



