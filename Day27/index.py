import mysql.connector 
from db import info

try:
    conn=mysql.connector.connect(**info)
    print("connection done")
except:
    print("not able to connect")

cursor=conn.cursor() 

# query='CREATE DATABASE IF NOT EXISTS INSTAGRAM'
# cursor.execute(query)

cursor.execute('use INSTAGRAM')
# create_table="""create table if not  exists users(
# user_id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(30) NOT NULL UNIQUE,
#     password_hash VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL UNIQUE,
#     posts_count INT DEFAULT 0,
#     likes_count INT DEFAULT 0,
#     followers INT DEFAULT 0,
#     following INT DEFAULT 0
# )"""

# cursor.execute(create_table)

# data=[
#     ('sathi_07','S@thi','sathi@gmail.com',7,100,200,250),
#     ('sagar','$aGar','sagar7@gmail.com',100,1000,700,290),
#     ('anu_priya','Anu@123','anupriya@example.com',25,  500,  800, 320),
#     ('raj_kumar','Raj@456','rajkumar@example.com',60, 2300, 1800, 710),
#     ('neha_dev', 'Neha@789','nehadev@example.com', 15,  750,  900, 280),
#     ('photo_sam','Sam@111','photosam@example.com',90, 4200, 3500, 950),
#     ('foodie_me','Food@007','foodieme@example.com',30, 1100, 1300, 400)

# ]

# query="insert into users(username,password_hash,email,posts_count,likes_count,followers,following) values(%s,%s,%s,%s,%s,%s,%s)"


# cursor.executemany(query,data)


# update_query = "UPDATE users SET followers = followers + 500 WHERE username = %s"
# cursor.execute(update_query, ("sathi_07",))
# print("Followers updated!")


delete_query = "DELETE FROM users WHERE username = %s"
cursor.execute(delete_query, ("photo_sam",))
print("User deleted!")


conn.commit()
cursor.close()
conn.close()