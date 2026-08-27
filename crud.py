import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='indigo')
    mycursor = conn.cursor()
    # print('Connected to MySQL')

except:
    print('Could not connect to MySQL')

# create a database on the db server
# mycursor.execute('CREATE DATABASE indigo')
# conn.commit()

# create a table
# airport -> airport_id | code | name | city
# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """)
# conn.commit()

# Insert data to the table
# mycursor.execute("""
#     INSERT INTO airport VALUES
#     (1,'DEL', 'New Delhi', 'IGIA'),
#     (2,'CCU', 'Kolkata', 'NSCA'),
#     (3, 'BOM', 'Mumbai', 'CSMA')
# """)
# conn.commit()

# search/retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# update
# mycursor.execute("""
#     UPDATE airport
#     SET city = 'Bombay'
#     WHERE city = 'Mumbai'
# """)
# conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("""
    DELETE FROM airport
    WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)