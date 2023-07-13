import pytest
import sqlite3
from datetime import datetime as dt

# Import the functions from the code you want to test
import database as db

# Define the test cases

# Test save_link function

def test_save_link():

    # defining the test values
    full_url = 'https://example.com'
    short_url = 'abcd'

    # Call the save_link function with test data
    db.save_link(full_url, short_url)

    # Connect to the test database
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    
    # Query the database to check if the link was saved correctly
    cursor.execute(f'SELECT * FROM links WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()

    # Close the cursor and commit the changes
    cursor.close()
    conn.commit()
    
    # Close the connection
    conn.close()
    
    # Assert the result matches the expected values
    assert result[1] == 'https://example.com'
    assert result[2] == 'abcd'



# Test get_original_url function


# def test_get_original_url():
#     # Connect to the test database
#     conn = sqlite3.connect('links.db')
#     cursor = conn.cursor()

#     # Insert test data into the links table
#     cursor.execute('INSERT INTO links (original_url, short_url) VALUES (?, ?)',
#                    ('https://example.com', 'abcd'))

#     # Call the get_original_url function with the test short URL
#     result = get_original_url('abcd')

#     # Assert the result matches the expected original URL
#     assert result == 'https://example.com'

#     # Close the connection
#     conn.close()

# # Test is_short_url_unique function


# def test_is_short_url_unique():
#     # Connect to the test database
#     conn = sqlite3.connect('links.db')
#     cursor = conn.cursor()

#     # Insert test data into the links table
#     cursor.execute('INSERT INTO links (original_url, short_url) VALUES (?, ?)',
#                    ('https://example.com', 'abcd'))

#     # Call the is_short_url_unique function with the test short URL
#     result = is_short_url_unique('abcd')

#     # Assert the result is False since the short URL already exists
#     assert result is False

#     # Close the connection
#     conn.close()

# # Test log_url_redirect function


# def test_log_url_redirect():
#     # Connect to the test database
#     conn = sqlite3.connect('links.db')
#     cursor = conn.cursor()

#     # Call the log_url_redirect function with test data
#     log_url_redirect('abcd')

#     # Query the database to check if the log entry was created
#     cursor.execute('SELECT * FROM request_log')
#     result = cursor.fetchone()

#     # Assert the result matches the expected values
#     assert result[1] == 'abcd'
#     assert isinstance(dt.strptime(result[2], '%Y-%m-%d %H:%M:%S'), dt)

#     # Close the connection
#     conn.close()

# # Test redirect_count function


# def test_redirect_count():
#     # Connect to the test database
#     conn = sqlite3.connect('links.db')
#     cursor = conn.cursor()

#     # Insert test data into the request_log table
#     cursor.execute(
#         'INSERT INTO request_log (short_url, datetime_accessed) VALUES (?, ?)', ('abcd', dt.now()))

#     # Call the redirect_count function with the test short URL
#     result = redirect_count('abcd')

#     # Assert the result is 1 since there is one redirect entry
#     assert result == 1

#     # Close the connection
#     conn.close()


# Run the tests
pytest.main(["-v", "--tb=line", "-rN", __file__])