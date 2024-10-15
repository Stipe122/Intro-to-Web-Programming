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

# if (params.getvalue("name") == None or params.getvalue("email") == None or params.getvalue("password") == None or params.getvalue("password2") == None):
#     # set cookie error message to some information is missing
#     cookie = cookies.SimpleCookie()
#     cookie["message"] = "Some information is missing"
#     print(cookie.output())
#     print("Location: ./registracija.py\n\n")

    # Destroj session 
    # db.destroy_session(session_id)

# Destroy user id cookie
cookie = cookies.SimpleCookie()
cookie["loginStatus"] = 0
cookie["korisnik"] = ""
cookie["id"] = ""
print(cookie.output())




if (params):
    nameRes = db.checkName(params)
    emailRes = db.checkEmail(params)
    if (emailRes != None and params.getvalue("email") != None):
        # set cookie error message to wrong email
        cookie = cookies.SimpleCookie()
        cookie["message"] = "Email already exists"
        print(cookie.output())
        print("Location: ./registracija.py\n\n")
    elif (nameRes != None and params.getvalue("name") != None):
        # set cookie error message to wrong name
        cookie = cookies.SimpleCookie()
        cookie["message"] = "Name already exists"
        print(cookie.output())
        print("Location: ./registracija.py\n\n")
    elif (params.getvalue("password") != params.getvalue("password2") and params.getvalue("password") != None and params.getvalue("password2") != None):
        # set cookie error message to passwords dont match
        cookie = cookies.SimpleCookie()
        cookie["message"] = "Passwords dont match"
        print(cookie.output())
        print("Location: ./registracija.py\n\n")
    else:
        # Insert user into db
        db.registerUser(params)
        # clear cookie message
        cookie = cookies.SimpleCookie()
        cookie["message"] = ""
        print(cookie.output())


print("Content-type:text/html\r\n\r\n")
print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IWA - Vjezba 4</title>
    </head>
    <body>
    <form action="./index.py" method="post">
    ''')

# Print username and password inputs

print(""" 
Username: 
<br> <br>
<input type="text" name="username"/>
<br> <br>
Password: 
<br> <br>
<input type="password" name="password"/>
""")

# Log in button

print("""
<br> <br>
<input type="submit" name"login" value="Login"/>
""")

# link sa registraciju i zaboravljenu lozinku

print("""
<br> <br>
<a href="./registracija.py">Registracija</a>
<br> <br>
<a href="./forgotPassword.py">Zaboravljena lozinka</a>
<br> <br>
""")

# Print error message from cookie if it exists
if (all_cookies_object.get("loginError")):
    if (all_cookies_object.get("loginError").value != None):
        print("""
        <h3>
        """ + all_cookies_object.get("loginError").value + """</h3>""")

base.end_html_form()
