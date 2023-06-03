import sqlite3
import datetime

# Create a connection to the database
conn = sqlite3.connect('links.db')
# Create a cursor object to execute SQL commands
cursor = conn.cursor()
# Create a table to store links if it doesn't already exist
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
conn = sqlite3.connect('request_log.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS request_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_url TEXT NOT NULL,
        datetime_accessed TEXT NOT NULL
    )
''')
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
    cursor.execute(
        'SELECT original_url FROM links WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None


def is_short_url_unique(short_url):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT COUNT(short_url) FROM links WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    cursor.close()
    if result[0] >= 1:
        return False
    else:
        return True


def log_url_redirect(short_url):
    now = datetime.datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('request_log.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO request_log (short_url, datetime_accessed) VALUES (?, ?)', (short_url, current_time))
    conn.commit()
    conn.close()

def redirect_count(short_url):
    conn = sqlite3.connect('request_log.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM request_log WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None