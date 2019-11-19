import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host = "localhost"
username = ""
password = ""
dbname = ''

mydb = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=dbname
)
# 
# 
# 
mycursor = mydb.cursor()
print("Question 1 - Find users that are not assigned to any company")
mycursor.execute('select * FROM users WHERE companyID IS NULL')
myresult = mycursor.fetchall()

for x in myresult:
     print(x)
# 
# 
# 
print("Question 2 - Find active (not deleted) users who are assigned to inactive (deleted) companies")
mycursor.execute('select * from users b WHERE isDeleted = 0 AND EXISTS ( select * from companies a WHERE a.isDeleted = 1 AND b.companyId = a.id )')
myresult = mycursor.fetchall()

for x in myresult:
     print(x)
# 
# 
# 
print("Question 3 - Find out how many active (not deleted) users are assigned to each active (not deleted) company. Display the list of company names and the number of active users in descending order")
mycursor.execute('select b.name, count(*) from companies b JOIN users a ON b.id = a.companyId WHERE a.isDeleted = 0 AND b.isDeleted = 0 GROUP BY b.name DESC')
myresult = mycursor.fetchall()

for x in myresult:
     print(x)
# 
# 
# 
print("Question 4 - Find users that are assigned to a non-existent company.")
mycursor.execute('select * from users b WHERE NOT EXISTS ( select * from companies a WHERE b.companyId = a.id )')
myresult = mycursor.fetchall()

for x in myresult:
     print(x)
# 
# 
# 
print("Question 5 - Create a new user, Leto, assigned to ‘A-Corp’")
q = ("INSERT INTO users (name, companyId, isDeleted) VALUES (%s, %s, %s) ")
val = ('Leto', 1, 0)
mycursor.execute(q, val)
mydb.commit()
print ("1 record inserted, ID: ", mycursor.lastrowid)
# 
# 
# 
print("Question 6 - Change Leto’s name to Leo. ")
sql = "UPDATE users SET name = 'Leo' WHERE name = 'Leto'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) updated")
# 
# 
# 
print("Question 8 - Delete user Bob ")
sql = "DELETE FROM users where name = 'Bob';"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")






