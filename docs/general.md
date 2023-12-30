# General Function Documentation & Description

## Python Flask Library Use
This project uses the Flask, a simple web-microframework. All the code that uses [Flask](https://flask.palletsprojects.com/en/3.0.x/) is located in the [app.py](../app.py) file. Here is breakdown of the functions.

### home()
- The is the page that is served when the user access the root of the application. Nothing too interesting happens here other than serving the [index.html](../templates/index.html) page.
- The button on the page brings the user to the /shortener url serving the [shorten-form.html](../templates/shorten-form.html) page.

### shorten_form()
- There is a form with a text box entry on this [shorten-form.html](../templates/shorten-form.html) page that posts the form response with the entered URL to Flask. 
- That above all happens in the html served by this function. 

### shorten()
- Gets the user entered URL from the POST request. The function then calls generate_short_url() to get a shortened subpage code. 
- Uses the imported database object to make sure that the short code generated is unique and not already in the database. 
- Logs the short code with the destination URL in the database. 
- Renders the [shortened.html](../tempaltes/shortened.html) page with the new URL with the short code on it that the user can then copy or click on. 

### generate_short_url()
- Generates a random short 6 character code and returns it. 

### redirect_to_url()
- Gets the origional URL from the database object. 
- Checks to make sure that there is either a valid https or http protocal at the start of the URL. If not, adds https.
- If a URL came back from the database object, redirect the user using 302 (temporary) redirect. 
- If no URL came back then serve the [404.html](../templates/404.html) page indicating that no URL was found. 

## Python SQLite3 Library Use

### Object Import/Creation
- Connects to the database files and checks to make sure that the tables already exist. If they do not exist, it runs a query to create them and then commits changes and closes the connection. 

### save_link()
- Writes a query to the database with the given short code and origional URL that writes it as an entry and commits the changes and closes the connection. 

### get_origional_url()
- Takes in a string short code value and queries the database for the corresponding URL that should have been written in the entry with it the closes the connection. 
- If there was a result, return it, otherwise return null.

### is_short_url_unique()
- Queries the database for a corosponding URL with the inputted short URL. 
- If there is a result, indicating that the given shortcode is not unique, then return False. 
- If there was no result, return True. 

### log_url_redirect()
- Log the redirect request in the requests log database, and closes the connection. 

### redirect_count()
- Counts the amount of times that a URL was redurected to in the request log databse and returns the initger value. 