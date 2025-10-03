import mysql.connector 
from db import info

try:
    conn=mysql.connector.connect(**info)
    print("connection done")
except:
    print("not able to connect")

cursor=conn.cursor()  
#creating a database
query='CREATE DATABASE IF NOT EXISTS 10000KCODERS'
cursor.execute(query)

#useing data bases
cursor.execute('use 10000KCODERS')

#create a table 
create_table="""create table if not exists students( 
id int auto_increment primary key,name varchar(50),email varchar(50),
courser varchar(50),join_date date)"""

cursor.execute(create_table)

# # #insert data into table like statict way


insert_data="""insert into students(name,email,courser,join_date) values("sathish","sathi@gmail.com","MERN","2025-06-13")"""

cursor.execute(insert_data)

# #Insert multiple valuse at a like a Dymanic way
students = [
    ("sathish", "sathi@gmail.com", "MERN", "2025-06-13"),
    ("akhil", "akhil@gmail.com", "Python", "2025-06-14"),
    ("prasad", "prasad@gmail.com", "Java", "2025-06-15"),
    ("raju", "raju@gmail.com", "React", "2025-06-16"),
    ("sagar", "sagar@gmail.com", "NodeJS", "2025-06-17"),
]

# # parameterized query
query = "INSERT INTO students (name, email, courser, join_date) VALUES (%s, %s, %s, %s)"

# insert all at once
cursor.executemany(query, students)

# #BY USING THE FUNCTIONS
# def multi_row_insert(studets):
#     query = "INSERT INTO students (name, email, courser, join_date) VALUES (%s, %s, %s, %s)"

# multi_row_insert(  [("kiran", "kiran@gmail.com", "Angular", "2025-06-18"),
#     ("teja", "teja@gmail.com", "Django", "2025-06-19"),
#     ("swathi", "swathi@gmail.com", "Flutter", "2025-06-20"),
#     ("mani", "mani@gmail.com", "C#", "2025-06-21"),
#     ("rekha", "rekha@gmail.com", "AI/ML", "2025-06-22"),
# ])

# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()

# print("\n--- Student Records ---")
# for i in rows:
#     print(i)

# mern_students = [student for student in rows if student[3] == "MERN"]

# print("\n--- MERN Students ---")
# for student in mern_students:
#     print(student)
        


# #use where condtion,group by to filter the cources,count same cource students,perform operations 

# # write the whole code in try,exception block

# import mysql.connector
# from db import info

# def multi_row_insert(cursor, students):
#     """Insert multiple rows dynamically into students table"""
#     query = "INSERT INTO students (name, email, courser, join_date) VALUES (%s, %s, %s, %s)"
#     cursor.executemany(query, students)


# try:
#     # connect to DB
#     conn = mysql.connector.connect(**info)
#     cursor = conn.cursor()
#     print("Connection done")

#     # create DB
#     cursor.execute('CREATE DATABASE IF NOT EXISTS 10000KCODERS')
#     cursor.execute('USE 10000KCODERS')

#     # create table
#     create_table = """
#     CREATE TABLE IF NOT EXISTS students(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(50),
#         email VARCHAR(50),
#         courser VARCHAR(50),
#         join_date DATE
#     )
#     """
#     cursor.execute(create_table)

#     # insert multiple students
#     students = [
#         ("sathish", "sathi@gmail.com", "MERN", "2025-06-13"),
#         ("akhil", "akhil@gmail.com", "Python", "2025-06-14"),
#         ("prasad", "prasad@gmail.com", "Java", "2025-06-15"),
#         ("raju", "raju@gmail.com", "React", "2025-06-16"),
#         ("sagar", "sagar@gmail.com", "NodeJS", "2025-06-17"),
#     ]
#     cursor.executemany("INSERT INTO students (name, email, courser, join_date) VALUES (%s, %s, %s, %s)", students)

#     # insert via function
#     more_students = [
#         ("kiran", "kiran@gmail.com", "Angular", "2025-06-18"),
#         ("teja", "teja@gmail.com", "Django", "2025-06-19"),
#         ("swathi", "swathi@gmail.com", "Flutter", "2025-06-20"),
#         ("mani", "mani@gmail.com", "C#", "2025-06-21"),
#         ("rekha", "rekha@gmail.com", "AI/ML", "2025-06-22"),
#     ]
#     multi_row_insert(cursor, more_students)

#     # commit inserts
#     conn.commit()

#     # fetch all students
#     cursor.execute("SELECT * FROM students")
#     rows = cursor.fetchall()
#     print("\n--- All Student Records ---")
#     for r in rows:
#         print(r)

#     # filter MERN students (Python-side)
#     mern_students = [student for student in rows if student[3] == "MERN"]
#     print("\n--- MERN Students (Python filter) ---")
#     for student in mern_students:
#         print(student)

#     # filter MERN students (SQL-side)
#     cursor.execute("SELECT * FROM students WHERE courser = 'MERN'")
#     mern_sql = cursor.fetchall()
#     print("\n--- MERN Students (SQL WHERE) ---")
#     for student in mern_sql:
#         print(student)

#     # group by course + count
#     cursor.execute("SELECT courser, COUNT(*) as total FROM students GROUP BY courser")
#     course_counts = cursor.fetchall()
#     print("\n--- Student Count by Course ---")
#     for c in course_counts:
#         print(c[0], "=>", c[1])

# except mysql.connector.Error as e:
#     print(" Database Error:", e)

# except Exception as e:
#     print(" Other Error:", e)

# finally:
#     if 'cursor' in locals():
#         cursor.close()
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()
#         print("\nConnection closed")


# def get_limit(limit):
#     try:
#         query="""select * from students limit %s """
#         cursor.execute(query,(limit,))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("Worng")
# get_limit(5)    

def update_by_email(cursor, courser, email):
    try:
        query = "UPDATE students SET courser = %s WHERE email = %s"
        cursor.execute(query, (courser, email))
        print(f"Updated {email} to course {courser}")
    except Exception as e:
        print("Error:", e)

# Usage
update_by_email(cursor, 'sqldeveloper', 'sagar@gmail.com')
conn.commit()  # Commit after update


def updatenamecoursebyemail(cursor, new_name, new_course, email):
    """
    Update a student's name and course based on their email.
    """
    try:
        query = "UPDATE students SET name = %s, courser = %s WHERE email = %s"
        cursor.execute(query, (new_name, new_course, email))
        print(f"Updated student {email} to Name: {new_name}, Course: {new_course}")
    except Exception as e:
        print("Error updating student:", e)

# Example usage:
updatenamecoursebyemail(cursor, "Sagar Ejjagiri", "mongodb Developer", "sagar@gmail.com")
conn.commit()  # Don't forget to commit the changes


def deleterecord_byid(id):
    try:
        query="""delete from students where id = %s"""
        cursor.execute(query,(id,))
        print("Done")
    except:
        print("Worng")
deleterecord_byid(2)    

def deleterecord_by_email(email):
    try:
        query="""delete from students where email = %s"""
        cursor.execute(query,(email,))
        print("Done")
    except:
        print("Worng")
deleterecord_by_email('akhil@gmail.com')
conn.commit()
cursor.close()
conn.close()