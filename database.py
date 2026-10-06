import sqlite3
conn=sqlite3.connect("database.db");
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,branch TEXT)""")
students=[(1,"Haasini",21,"AI & DS"),
          (2,"Shannu",20,"CSE"),
          (3,"Sahithi",21,"AI & DS"),
          (4,"Pranathi",20,"AI & ML"),
          (5,"Bhavya",21,"ECE")
          
]
cursor.executemany("""INSERT OR IGNORE INTO students(id,name,age,branch)VALUES(?,?,?,?)""",students)
conn.commit()
print("Database created successfully")
print("Students table created successfully")
cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()