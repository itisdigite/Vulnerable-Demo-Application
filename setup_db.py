import sqlite3
import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT
    )
''')

# List of 10 random usernames and passwords
credentials = [
    ('john_doe', 'P@ssw0rd123', 'user'),
    ('alice_smith', 'SecureP@ss1', 'user'),
    ('bob_wilson', 'B0bP@ssw0rd', 'user'),
    ('emma_jones', 'J0nesP@ss!', 'user'),
    ('michael_brown', 'Br0wnP@ss!', 'user'),
    ('sarah_davis', 'D@visP@ss1', 'user'),
    ('david_miller', 'M1llerP@ss', 'user'),
    ('lisa_taylor', 'T@ylorP@ss', 'user'),
    ('james_anderson', 'And3rs0nP@ss', 'user'),
    ('admin', 'Adm!n@123.', 'admin'),
    ('admin', 'adminpass', 'admin'),
    ('user', 'userpass', 'user')
]

# Insert the credentials
for username, password, role in credentials:
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                  (username, password, role))

conn.commit()
conn.close()

print("Database setup complete with 10 user accounts.") 