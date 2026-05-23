import sqlite3

print("SQLite Imported Successfully")
conn = sqlite3.connect("students.db")

print("Database Connected")
cursor = conn.cursor()

print("Cursor Ready")
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()

print("Table Created Successfully")
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ")

        cursor.execute(
            "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )

        conn.commit()

        print("Student Added Successfully")

    elif choice == "2":

        cursor.execute("SELECT * FROM students")

        records = cursor.fetchall()

        print("\n--- STUDENT RECORDS ---")

        for row in records:
            print(row)

    elif choice == "3":
        search_name = input("Enter Student Name To Search: ")
        cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (search_name,)
        )
        records = cursor.fetchall()
        print("\n--- SEARCH RESULTS ---")
        for row in records:
            print(row)

    elif choice == "4":
        student_id = int(input("Enter Student ID To Delete: "))
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )
        conn.commit()
        print("Student Deleted Successfully")

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

#conn.close()
#print("Database Connection Closed")
