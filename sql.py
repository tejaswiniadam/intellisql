import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS (
NAME TEXT,
CLASS TEXT,
MARKS INT
)
""")

cursor.execute("INSERT INTO STUDENTS VALUES ('Teja', 'BTech', 85)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Ravi', 'BSc', 78)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Anu', 'BCom', 90)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Kiran', 'BTech', 92)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Priya', 'BSc', 88)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Rahul', 'BCom', 76)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Sneha', 'BTech', 95)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Arjun', 'BSc', 81)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Divya', 'BCom', 84)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Vikram', 'BTech', 73)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Meena', 'BSc', 89)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Suresh', 'BCom', 67)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Neha', 'BTech', 91)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Ajay', 'BSc', 79)")
cursor.execute("INSERT INTO STUDENTS VALUES ('Pooja', 'BCom', 86)")



conn.commit()
conn.close()

print("Database created")
