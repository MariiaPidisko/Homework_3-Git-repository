import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute(
    '''CREATE TABLE emails
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(25));''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()