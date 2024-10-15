#!python.exe
import session
import subjects
import base
import os
import cgi
import db
import password_utils
from http import cookies

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

params = cgi.FieldStorage()

errorMsg = ""

if (params):
    # Check given email if not found return error message
    emailRes = db.checkEmail(params)
    passwordRes = db.checkPasswordForReset(params)

    if (emailRes == None):
        cookie = cookies.SimpleCookie()
        cookie["forgotPasswordMessage"] = "Email not found"
        errorMsg = "Email not found"
        print(cookie.output())
    elif (params.getvalue("currentPassword") == None):
        errorMsg = "Please enter current password"
    # Check current password for given email if not same return error
    elif (params.getvalue("currentPassword") != None):
        password = params.getvalue("currentPassword")
        isValid = password_utils.verify_password(password, passwordRes[0])
        if (isValid == False):
            errorMsg = "Current password is incorrect"
        else:
            # Check if new password and new password2 are same
            if (params.getvalue("password") == None or params.getvalue("password2") == None):
                errorMsg = "Please enter password"
            elif (params.getvalue("password") != params.getvalue("password2")):
                errorMsg = "Passwords are not the same"
            elif (params.getvalue("password") == password):
                errorMsg = "Your new password cant be same as your old password"
            else:
                # Remove errorMsg and errorMsg cookie
                cookie = cookies.SimpleCookie()
                cookie["forgotPasswordMessage"] = ""
                errorMsg = ""
                print(cookie.output())

                # set user password to new password hash
                db.resetUserPassword(params, emailRes[1])
                print("Location: ./prijava.py\n\n")


# print("Location: ./prijava.py\n\n")

print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IWA - Vjezba 4</title>
    </head>
    <body>
    <form action="" method="post">
    ''')

# Check for error messages
if (errorMsg != ""):
    print("""
        <h3>
        """ + errorMsg + """</h3>""")

# Print username and password inputs

print(""" 
Email: 
<br> <br>
<input type="text" name="email"/>
<br> <br>
Current password: 
<br> <br>
<input type="password" name="currentPassword"/>
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
<input type="submit" name"register" value="Promijeni lozinku"/>
""")

# link sa registraciju i zaboravljenu lozinku

print("""
<br> <br>
<a href="./prijava.py">Log in</a>
""")


base.end_html_form()
