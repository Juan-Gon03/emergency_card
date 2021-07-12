import sqlite3

con = sqlite3.connect('database/cards.db')

cur = con.cursor()
# Create table
fromName = "Alex"
toName = "Jose"
message = "hai!!!!"
holiday = "Birthday"

data = {(fromName, toName, message, holiday)}

cur.execute('''CREATE TABLE Birthday
              (id integer PRIMARY KEY, from_name text, to_name text, message text, holiday text)''')
cur.execute('''CREATE TABLE Chrismas
              (id integer PRIMARY KEY, from_name text, to_name text, message text, holiday text)''')
cur.execute('''CREATE TABLE New_Years
              (id integer PRIMARY KEY, from_name text, to_name text, message text, holiday text)''')
cur.execute('''CREATE TABLE Halloween
              (id integer PRIMARY KEY, from_name text, to_name text, message text, holiday text)''')
#cur.executemany("INSERT INTO card_values (from_name,to_name,message,holiday) VALUES(?,?,?,?)", data)

  # Save (commit) the changes
con.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
'''for row in cur.execute('SELECT * FROM card_values ORDER BY id'):
    print(row)'''

con.close()
