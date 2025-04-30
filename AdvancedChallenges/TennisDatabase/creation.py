import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("database.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS undereleven (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    lcp INTEGER
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")