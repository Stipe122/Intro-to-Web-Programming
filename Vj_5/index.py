#!python.exe

import cgi
import os
import base
import subjects
import session
import db
import password_utils
from http import cookies

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

params = cgi.FieldStorage()

# if (os.environ["REQUEST_METHOD"].upper() == "POST"):
#     session.add_to_session(params)

# session_data = session.get_session_data()

# dictionary = subjects.read_session_data(session_data)

# Current loggedIn user username
currentUser = ""

# Handle user login attempt
username = params.getvalue("username")
password = params.getvalue("password")

# Get user password from db
nameRes = db.checkUsername(params)
passwordRes = db.checkPassword(params)

# if (nameRes == None):
#     cookie = cookies.SimpleCookie()
#     cookie["loginError"] = str("Invalid user")
#     print(cookie.output())
#     print("Location: ./prijava.py\n\n")

if (params):
    # Compare password with hashed password from db if its not same redirect back to prijava.py
    if (params.getvalue("password")):
        isValid = password_utils.verify_password(password, passwordRes[0])
        if (isValid == False):
            cookie = cookies.SimpleCookie()
            cookie["loginError"] = str("Invalid password")
            cookie["loginStatus"] = 0
            print(cookie.output())
            print("Location: ./prijava.py\n\n")
        else:
            # if (os.environ["REQUEST_METHOD"].upper() == "POST"):
            #     session.add_to_session(params)
            # session_data = session.get_session_data()
            # dictionary = subjects.read_session_data(session_data)
            cookie = cookies.SimpleCookie()
            currentUser = nameRes[1]
            cookie["loginError"] = ""
            cookie["loginStatus"] = 1
            cookie["korisnik"] = nameRes[1]
            print(cookie.output())

    # # # # If user loged in cookie is false redirect to prijava
    # if (all_cookies_object.get("korisnik").value == ""):
    #     print("Location: ./prijava.py\n\n")
else:
    # # # If user loged in cookie is false redirect to prijava
    if (all_cookies_object.get("korisnik").value == ""):
        print("Location: ./prijava.py\n\n")

if (currentUser == ""):
    if (os.environ["REQUEST_METHOD"].upper() == "POST"):
        session.add_to_session(params)
    session_data = session.get_session_data()
    dictionary = subjects.read_session_data(session_data)

base.start_html_form()
print("""
<a href="./odjava.py">Odjava</a>
<br> <br>
""")

if (currentUser != ""):
    print("""<h3> Hej """ + currentUser + """</h3>""")

if (all_cookies_object.get("korisnik").value != ""):
    print("""<h3> Hej """ + all_cookies_object.get("korisnik").value + """</h3>""")

subjects.display_buttons()

if params.getvalue('button') == 'Enrollment List':
    subjects.print_enrollment_list(dictionary)
elif params.getvalue('button') != None:
    subjects.print_subjects_year(params.getvalue('button'), dictionary)
base.end_html_form()
