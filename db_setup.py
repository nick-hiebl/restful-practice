import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

c.execute('''CREATE TABLE accounts
(username text, password text, email text)''')
# Create the table

conn.commit()
conn.close()