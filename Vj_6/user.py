#!python.exe
import session
import subjects
import base
import os
import cgi
import db
from http import cookies

params = cgi.FieldStorage()

# Get user Id

userName = params.getvalue("user")
res = db.getUserId(userName)
userId = res[0]

print("Content-type:text/html\r\n\r\n")
print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IWA - Vjezba 4</title>
    </head>
    <body>
    ''')

print("""<h2>Upisni list korisnika """ + params.getvalue("user") + """</h2>""")
print("""<br><br>""")

# print(userId)

# Print user listž
subjects.print_user_enrollment_list(userId)
print("""<br><br>""")


# Print user upisni list
base.end_html_form()