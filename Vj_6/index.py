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

# Current loggedIn user username
currentUser = ""

# Handle user login attempt
username = params.getvalue("username")
password = params.getvalue("password")

# Get user password from db
nameRes = db.checkUsername(params)
passwordRes = db.checkPassword(params)


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
            # Popuni upisni list sa default podatcima ako vrijednost ne postoji
            curList = db.upisniListFromUserId(nameRes[0])
            if (curList == []):
                subjects.fillList(nameRes[0])
            cookie = cookies.SimpleCookie()
            currentUser = nameRes[1]
            cookie["loginError"] = ""
            cookie["loginStatus"] = 1
            cookie["korisnik"] = nameRes[1]
            cookie["id"] = nameRes[0]
            cookie["accessError"] = ""
            print(cookie.output())

else:
    # # # If user loged in cookie is false redirect to prijava
    if (all_cookies_object.get("korisnik").value == ""):
        print("Location: ./prijava.py\n\n")


# Get status predmeta iz baze po idu korisnika
userId = all_cookies_object.get("id")

# !!!!! On every page refresh check if params value is different from database
# !!!!! Check row by row
# !!!!! If it is -> change that row value status(not,pass,enr) to new value

# Get user user_list value
res = db.upisniListFromUserId(userId.value)

for row in res:
    # row[3] - status (not, enr, pass)
    # row[2] - predmet id
    # get predmet kod from predmetId
    subjectNames = db.getSubjectNameForListById(row[2])
    kod = subjectNames[2]
    # print(kod)
    newValue = params.getvalue(kod)
    oldValue = row[3]

    # print(newValue)
    # print(oldValue)
    # print("""<br><br>""")
    if (oldValue != newValue and newValue != None):
        # print("Razlicito")
        # Change row in db by predmet id
        db.changeUserListByPredmetId(userId.value, row[2], newValue)

# Check database row by row
# for row in res:


# Add not radio values to db for all subjects for user
# if (currentUser == ""):
# subjects.addToUpisniList()
# if (os.environ["REQUEST_METHOD"].upper() == "POST"):
#     session.add_to_session(all_cookies_object.get("korisnik").value)
# session_data = session.get_session_data()
# dictionary = subjects.read_session_data(session_data)

# Get input values and set them to curUser in db

base.start_html_form()

if (all_cookies_object.get("accessError")):
    if (all_cookies_object.get("accessError").value != None):
        print("""<h1>""" + all_cookies_object.get("accessError").value + """</h1>""")
        print("""<br><br>""")


print("""
<a href="./odjava.py">Odjava</a>
<br> <br>
""")

print("""
<a href="./popis_studenata.py">Popis studenata</a>
<br> <br>
""")

if (currentUser != ""):
    print("""<h3> Hej """ + currentUser + """</h3>""")

if (all_cookies_object.get("korisnik").value != ""):
    print("""<h3> Hej """ + all_cookies_object.get("korisnik").value + """</h3>""")

subjects.display_buttons()

if params.getvalue('button') == 'Enrollment List':
    # Test to see if you can get values of upisni list from user id
    # lista = db.upisniListFromUserId(userId.value)
    # print(lista)
    subjects.print_user_enrollment_list(userId.value)
    # Print from userlist db
    # subjects.print_enrollment_list(dictionary)
elif params.getvalue('button') != None:
    # Add value from userlist db
    # subjects.addToUpisniList()
    # print("button")
    # id = all_cookies_object.get("id").value
    # print(id)
    # role = db.get_user_role_enum(id)
    # print(role)
    subjects.print_subjects_year(params.getvalue('button'), userId.value)

base.end_html_form()
