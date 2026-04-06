import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE voters(
id INTEGER PRIMARY KEY AUTOINCREMENT,
voter_id TEXT UNIQUE,
voted INTEGER DEFAULT 0
)
""")

cur.execute("""
CREATE TABLE votes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
candidate TEXT
)
""")

voters = ["1001","1002","1003","1004","1005"]

for v in voters:
    cur.execute("INSERT INTO voters(voter_id) VALUES(?)",(v,))

conn.commit()
conn.close()

print("Database created successfully")