import sqlite3

conn = sqlite3.connect("cdss.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(patients);")

print(cursor.fetchall())

conn.close()