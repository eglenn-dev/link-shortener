import sqlite3
from datetime import datetime as dt

# ----------------------------------------------------------------
# Checking to make sure that the links.db database file exists.

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
# Checking to make sure that the requests_log.db database file exists.

# Create a connection to the database
conn = sqlite3.connect('request_log.db')
# Create a cursor object to execute SQL commands
cursor = conn.cursor()
# Creat a table to store links if it doesn't already exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS request_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_url TEXT NOT NULL,
        datetime_accessed TEXT NOT NULL
    )
''')
# Commit the changes and close the connection
conn.commit()
conn.close()

# ----------------------------------------------------------------

def save_link(original_url, short_url):
    ''' Takes in a original URL and the short reference URL 
    and stores it in the SQL database at next AI index. 
    Returns nothing.
    '''
    # Opening a connection to the links database
    conn = sqlite3.connect('links.db')
    # Creating a cursor object for executing the SQL queries.
    cursor = conn.cursor()
    # Executing the query that adds the information to the database.
    cursor.execute('INSERT INTO links (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
    # Committing the changes and closing the database connection.
    conn.commit()
    conn.close()

def get_original_url(short_url):
    ''' Takes in the short_url, queries the database for the 
    original url associated with the short one, and returns 
    the full length url if found.
    '''
    # Opening the connection to the links database
    conn = sqlite3.connect('links.db')
    # Creating a database object for executing SQL queries.
    cursor = conn.cursor()
    # Querying the database for the original url with the given short url and getting the result.
    cursor.execute('SELECT original_url FROM links WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    # Closing the database connection
    conn.close()
    # If there is a result from the query, return it, otherwise return None.
    if result:
        return result[0]
    else:
        return None

def is_short_url_unique(short_url):
    ''' Take in the short url and returns boolean True if it is 
    found in the database, otherwise return boolean False.
    '''
    # Opening a connection to the links database.
    conn = sqlite3.connect('links.db')
    # Creating a cursor object to query the database. 
    cursor = conn.cursor()
    # Querying the database for the short url 
    cursor.execute(
        'SELECT COUNT(short_url) FROM links WHERE short_url = ?', (short_url,))
    # Storing the result from the query
    result = cursor.fetchone()
    # Closing the connection to the database
    cursor.close()
    # If there is a result from the query, return boolean true, otherwise return boolean false
    if result[0] >= 1:
        return False
    else:
        return True

def log_url_redirect(short_url):
    ''' Used to log each time a url is used for a redirect in the request_log database.
    The short url, the system datetime, is stored in the database at the next AI line.  
    '''
    # Getting the current date and time from the system
    now = dt.now()
    # Formatting the date and time
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    # Connecting to the request_log database
    conn = sqlite3.connect('request_log.db')
    # Making a cursor object for executing queries
    cursor = conn.cursor()
    # Executing a insert query into the database
    cursor.execute('INSERT INTO request_log (short_url, datetime_accessed) VALUES (?, ?)', (short_url, current_time))
    # Commiting the query changes to the database
    conn.commit()
    # Closing the connection to the request_log database
    conn.close()

def redirect_count(short_url):
    ''' Takes in a short_url and returns the number of redirects from the 
    request_logs database. 
    '''
    # Opening a connection to the request_log database
    conn = sqlite3.connect('request_log.db')
    # Creating the cursor object for executing queries against the database
    cursor = conn.cursor()
    # Executing a SELECT query against the database and storing the results
    cursor.execute('SELECT count(*) FROM request_log WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    # Closing the connection to the database
    conn.close()
    # If there is a result, return it, otherwise return None
    if result:
        return result[0]
    else:
        return None