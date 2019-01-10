try: 
    with open("lmn.txt", "r") as f: 
        try:
            raise TypeError
        except TypeError: 
            print("Went to __exit__ of _io.TextIOWrapper first but got reraised") 
        for line in f: 
            print(line) 
except FileNotFoundError: 
    print("File lmn.txt does not exist") 

