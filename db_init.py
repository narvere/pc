import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, keepass INTEGER, sms INTEGER)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
