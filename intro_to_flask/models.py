#Importing database module,creating a table in database and inserting records in the table
import sqlite3 as sql


conn = sql.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE if not exists visitorstable3 (firstname TEXT,lastname TEXT, email TEXT, phoneno INTEGER, visiting TEXT)''')
print "Table created successfully";
conn.close()

def insert_visitor(firstname,lastname,email,phoneno,visiting):
    with sql.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO visitorstable3 (firstname,lastname,email,phoneno,visiting) VALUES (?,?,?,?, ?)", (firstname,lastname,email,phoneno,visiting) )
        con.commit()





        

        
    
    
    
            
    
  