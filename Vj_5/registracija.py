#!python.exe
import session
import subjects
import base
import os
import cgi
import db

from http import cookies

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

params = cgi.FieldStorage()

print("Content-type:text/html\r\n\r\n")
print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IWA - Vjezba 4</title>
    </head>
    <body>
    <form action="./prijava.py" method="post">
    ''')

# Print error message from cookie if it exists
if (all_cookies_object.get("message")):
    if (all_cookies_object.get("message").value != None):
        print("""
        <h3>
        """ + all_cookies_object.get("message").value + """</h3>""")


# Print username and password inputs

print("""
<br> <br>
Ime:
<br> <br>
<input type="text" name="name"/>
<br> <br>
Email:
<br> <br>
<input type="text" name="email"/>
<br> <br>
Password:
<br> <br>
<input type="password" name="password"/>
<br> <br>
Confirm password:
<br> <br>
<input type="password" name="password2"/>
""")

# Log in button

print("""
<br> <br>
<input type="submit" name"register" value="Register"/>
""")

# link sa registraciju i zaboravljenu lozinku

print("""
<br> <br>
<a href="./prijava.py">Log in</a>
""")

base.end_html_form()
