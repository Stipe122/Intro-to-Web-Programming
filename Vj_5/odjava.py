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

# Delete session from db

# # Delete session_id cookie
# cookies_object = cookies.SimpleCookie()
# cookies_object["session_id"] = None
# print(cookies_object.output())  # upisivanje cookie-a u header

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

print("""
<input type="submit" name"login" value="Odjava"/>
""")

base.end_html_form()
