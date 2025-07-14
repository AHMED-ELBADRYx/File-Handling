# Delete saved file

import os

# The name of the file you want to delete
db_file = "my_database.db"

# Check if the file exists, then delete it
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"{db_file} has been successfully deleted.")
else:
    print("The file does not exist.")
