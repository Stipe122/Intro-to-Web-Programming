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

id = all_cookies_object.get("id").value
role = db.get_user_role_enum(id)

if(role != "admin"):
    # Set error msg to cant acces if not admin
    cookie = cookies.SimpleCookie()
    cookie["accessError"] = "You cant access that page if you are not admin"
    print(cookie.output())
    print("Location: ./index.py\n\n")

print("Content-type:text/html\r\n\r\n")
print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IWA - Vjezba 4</title>
    </head>
    <body>
    ''')

# Get all users from db
res = db.getAllUsers()

# print(res[1])
# Print a hrefs with all users
for user in res:
    # print("""<a href='./user.py'>""" + user[0] + """</a>""")
    print("""<a href='""" + """./user.py?user=""" + user[0] + """'>""" + user[0] + """</a>""")
    print("""<br><br>""")





base.end_html_form()