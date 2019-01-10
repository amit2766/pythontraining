#! /usr/bin/python3 

import sys, StudentRecordDb, StudentRecord  

def main (): 

    db = StudentRecordDb.StudentRecordDb () 
    db.add (StudentRecord.StudentRecord ("Yogeshwar", 10, "Pune")) 
    db.add (StudentRecord.StudentRecord ("Rohit", 11, "Mumbai"))
    db.add (StudentRecord.StudentRecord ("Pratik", 12, "Nagpur"))
    db.add (StudentRecord.StudentRecord ("xyz", 13, "pqr"))
    db.add (StudentRecord.StudentRecord ("abc", 14, "lmn"))

    db.dump_all () 
    
    s = db.search (100)
    if s is None: 
        print ("Record with roll 100 Not Found") 
    s = db.search (12)
    if s is None: 
        print ("Record with roll 12 Not Found") 
    else:
        s.dump () 
    
    try:
        db.delete (100)
    except ValueError: 
        print ("Db trolled on purpose, no record with roll 100") 

    db.delete (11) 
    db.dump_all () 

    db.edit (14)
    db.dump_all () 

    sys.exit (0) 

if __name__ == '__main__': 
    main()

