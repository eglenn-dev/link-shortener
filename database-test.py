import sqlite3
import database

def main():
    print_db_contents('links.db')
    short_url = input(f'Short URL to check: ')
    check_get_original(short_url)
    check_if_in_db(short_url)

def print_db_contents(db_path):
    # Establish a connection to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM links")

    # Fetch the results
    results = cursor.fetchall()

    # Iterate over the results and print them
    for row in results:
        print(row)

    # Close the connection
    conn.close()

def check_if_in_db(short_url):
    if (database.is_short_url_unique(short_url)): print('URL is unique')
    else: print('URL is NOT unique')

def check_get_original(short_url):
    print(database.get_original_url(short_url))

if __name__ == '__main__':
    main()