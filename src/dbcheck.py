import sqlite3

con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()

query = "SELECT * FROM auth_user WHERE username='bob'"
cursor.execute(query)

print(cursor.fetchall())