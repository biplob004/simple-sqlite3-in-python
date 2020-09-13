import sqlite3
conn = sqlite3.connect('examveda.db')

c = conn.cursor()

# create a simple table with question and answer as coulumn names, of data type as text. And table name is table_name
c.execute("Create table if not exists table_name (question text, ans text)") 
conn.commit()


# inserting data into the table 
c.execute("Insert into table_name values (?,?)", ("What is your name? ", "My name is biplob das."))
conn.commit()
    

# display table data
value = c.execute("Select * from table_name").fetchall()
for v in value:
    print(v)


conn.close()
