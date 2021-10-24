import sqlite3

conn = sqlite3.connect('database.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE DATA
         (ID INT PRIMARY KEY     NOT NULL,
         CONTENT           TEXT    NOT NULL);''')

print("Table created successfully")

#Hello world in English
conn.execute("INSERT INTO DATA(ID,CONTENT) \
      VALUES (1, 'Hello World')")

#Hello world in Portuguese
conn.execute("INSERT INTO DATA(ID,CONTENT) \
      VALUES (2, 'Ola Mundo')")

conn.commit()

print("Records created successfully")
print("=================================")

cursor = conn.execute("SELECT id, content from DATA ")
for row in cursor:
    print("content:", row[1])

conn.close()
