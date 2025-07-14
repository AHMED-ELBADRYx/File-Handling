# Practical example of databases and cursor usage: SELECT | INSERT | UPDATE | DELETE

import sqlite3

def get_all_data():
    try:
        # Connect To Database
        db = sqlite3.connect("app.db")

        # Print Success Message
        print("Connected To Database Successfully")

        # Setting Up The Cursor
        cr = db.cursor()

        # Create Table
        cr.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, name TEXT)")

        # Members List
        members = ["Emad", "Ali", "Omar", "Ahmed", "Saif", "Adel"]

        # Loop On Members
        for key, user in enumerate(members):
            cr.execute("INSERT INTO users(user_id, name) VALUES (?, ?)", (key + 1, user))

        # Record Update
        cr.execute("UPDATE users SET name = 'Nader' WHERE user_id = 1")

        # Record Delete
        cr.execute("DELETE FROM users WHERE user_id = 2")

        # Save Variable
        db.commit()

        # Fetch Data From Database
        cr.execute("SELECT * FROM users")

        # Assign Data To Variable
        results = cr.fetchall()

        # Print Number Of Rows
        print(f"Database Has {len(results)} Rows.")

        # Printing Message
        print("Showing Data:")

        # Loop On Results
        for row in results:
            print(f"User ID => {row[0]},", end=" ")
            print(f"User Name => {row[1]}")

    except sqlite3.Error as er:
        print(f"Error Reading Data {er}")

    finally:
        if db:
            # Close Database Connection
            db.close()
            print("Connection To Database Is Closed")

get_all_data()