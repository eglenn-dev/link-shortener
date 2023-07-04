from flask import Flask, render_template, redirect, request
import string
import random
import database

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Serves the welcome index page
@app.route('/')
def home():
    # Returns the rendered index page
    return render_template('index.html')

# Serves the form shortener page
@app.route('/shortener')
def shorten_form():
    # Returns the shorten form page
    return render_template('shorten-form.html')

# Serves the shortened URL page
@app.route('/shorten', methods=['POST'])
def shorten():
    # gets the original URL from the user submitted form
    original_url = request.form['url']
    # Generate a shortened URL
    short_url = generate_short_url()
    while True:
        # Check if the generated shortened URL is already in the database
        if database.is_short_url_unique(short_url): break
        # If short URL is already in the database, generate a new one and check again
        else: short_url = generate_short_url()
    # Save the original and short URL to the database
    database.save_link(original_url, short_url)
    # Render the template with the redirected link return that to be displayed
    return render_template('shortened.html', short_url=short_url, original_url=original_url)

# Redirect to original URL
@app.route('/<short_url>')
def redirect_to_url(short_url):
    https = 'https://'
    http = 'http://'
    # Query the database for the original URL using the shortened URL
    original_url = database.get_original_url(short_url)
    # Checking to make sure that a value was returned from the database
    if original_url:
        # Checking if there is a https or http header on the url, if not then add https
        if (https not in original_url) and (http not in original_url):
            original_url = https + original_url
        # Log the redirect in the redirects database
        database.log_url_redirect(short_url)
        # Redirect the client to the original URL using a 302 (temporary) redirect
        return redirect(original_url, code=302)
    else:
        # If there was no return from the database query return a 404 error
        return render_template('404.html', short_url=short_url)

def generate_short_url():
    ''' Generate a short URL or random characters and numbers'''
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    # returns the random string
    return short_url

if __name__ == '__main__':
    # Runs the app on default port and on broadcasts on all channels.
    # This is done for deployment versions of the app. 
    app.run(port=5000, host='0.0.0.0')
    # For testing and debugging use the following line:
    # app.run(debug=True)