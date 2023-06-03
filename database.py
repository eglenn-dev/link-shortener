import sqlite3

# Create a connection to the database
conn = sqlite3.connect('links.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store links
cursor.execute('''
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_url TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# ----------------------------------------------------------------

def save_link(original_url, short_url):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO links (original_url, short_url) VALUES (?, ?)',
                   (original_url, short_url))
    conn.commit()
    conn.close()

def get_original_url(short_url):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute('SELECT original_url FROM links WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def is_short_url_unique(short_url):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(short_url) FROM links WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    cursor.close()
    if result[0] >= 1:
        return False 
    else: return True