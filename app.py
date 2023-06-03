from flask import Flask, render_template, redirect, request
import string
import random
import database

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Shorten URL
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_url = generate_short_url()
    while True:
        if database.is_short_url_unique(short_url): break
        else: short_url = generate_short_url()
    database.save_link(original_url, short_url)
    return render_template('shortened.html', short_url=short_url)

# Redirect to original URL
@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = database.get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "Invalid URL"

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

if __name__ == '__main__':
    app.run(debug=True)
