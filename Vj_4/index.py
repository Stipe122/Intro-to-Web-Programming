#!python.exe

import cgi
import os
import base
import subjects
import session

params = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

session_data = session.get_session_data()

dictionary = subjects.read_session_data(session_data)

base.start_html_form()
subjects.display_buttons()
if params.getvalue('button') == 'Enrollment List':
    subjects.print_enrollment_list(dictionary)
elif params.getvalue('button') != None:
    subjects.print_subjects_year(params.getvalue('button'), dictionary)
base.end_html_form()