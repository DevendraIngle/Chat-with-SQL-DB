import sqlite3

## connect to sqllite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Aryan','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ethan','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Rohan','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Liam','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Aditya','DEVOPS','A',35)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
