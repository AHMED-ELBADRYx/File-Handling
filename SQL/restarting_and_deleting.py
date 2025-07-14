# Reset the database and verify deletion of data from the users table

import sqlite3

# Connect to the database
conn = sqlite3.connect("my_database.db")  # Make sure the database name is correct
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

# Delete all data from the users table
cursor.execute("DELETE FROM users")

# Reset the ID counter (optional)
cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

conn.commit()

# Verify that the table is now empty
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
if not rows:
    print("All data has been deleted from the users table.")
else:
    print("There is still data in the users table:", rows)

conn.close()