import psycopg2
 
def create_table():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students(student_id SERIAL PRIMARY KEY, name TEXT, address TEXT, age INT, number TEXT);""")
    print("Student table created.")
    conn.commit()
    conn.close()
 
def insert_data():
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = int(input("Enter age: "))  # Ensure age is an integer
    number = input("Enter phone number: ")
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("""INSERT INTO students(name, address, age, number) VALUES (%s, %s, %s, %s)""", (name, address, age, number))
    print("Data inserted into student table.")
    conn.commit()
    conn.close()
 
def read_data():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    print("Displaying all student records:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Phone Number: {student[4]}")
    conn.close()
 
def update_data():
    student_id = input("Enter the ID of the student to be updated: ")
    field = input("Enter the field to update (name, address, age, number): ")
    new_value = input(f"Enter the new value for {field}: ")
    sql = f"UPDATE students SET {field} = %s WHERE student_id = %s"
    
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute(sql, (new_value, student_id))
    print(f"{field} updated successfully.")
    
    conn.commit()
    conn.close()
 
def delete_data():
    student_id = input("Enter the ID of the student to be deleted: ")
    
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    print("Student record deleted.")
    
    conn.commit()
    conn.close()
 
while True:
    print("\\nWelcome to the Student Management System")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
 
    if choice == '1':
        create_table()
    elif choice == '2':
        insert_data()
    elif choice == '3':
        read_data()
    elif choice == '4':
        update_data()
    elif choice == '5':
        delete_data()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")