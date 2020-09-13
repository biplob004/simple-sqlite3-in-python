import sqlite3
import random

random_id = random.random()

conn = sqlite3.connect('database_name.db')
c = conn.cursor()

# creating a simple table with question and answer as coulumn names, of data type as text. And table name is table_name
# here datatype can be null, integer, real, text, blob
c.execute("Create table if not exists table_name (sl_number real, question text, answer text)") 
conn.commit()


# inserting data into the table 
c.execute("Insert into table_name values (?,?,?)", (random_id, "What is your name? ", "My name is biplob das."))
conn.commit()

# # delete all from given table 
# c.execute("DELETE FROM table_name")
# conn.commit()

c.execute("UPDATE table_name SET question=? WHERE question=?", ("changed question?", "What is your name? "))
# OR 
# c.execute("UPDATE table_name SET question=?, ans=?  WHERE question=?", ("changed question?", "Changed answer", "What is your name? "))
conn.commit()
    
# display table data
value = c.execute("Select * from table_name").fetchall()

"""
Other select command exmples are:
c.execute("SELECT column_name1, column_name2 FROM table_name WHERE column_name3='hello'")
c.execute("SELECT * FROM table_name WHERE column_name1='hello'")
c.execute("SELECT * FROM table_name WHERE column_name1=?", ("hello"))

And in place of fetchall() you can use fetchone(), fetchmany(5)
"""

for v in value:
    print(v)
    


conn.close()
