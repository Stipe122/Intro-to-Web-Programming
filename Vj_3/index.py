#!python.exe

import base, subjects
import os, cgi
from http import cookies

params = cgi.FieldStorage()

year = params.getvalue("year_btn")
if not year:
    year = "1st Year"

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

for key in params:
  if key != "year_btn":
   cookie = cookies.SimpleCookie()
   cookie[key] = params.getvalue(key)
   print(cookie.output())

def print_navigation():
    print('''
    <form action="./index.py" method="POST">
      <input type="submit" name="year_btn" value="1st Year">
      <input type="submit" name="year_btn" value="2nd Year">
      <input type="submit" name="year_btn" value="3rd Year">
      <input type="submit" name="year_btn" value="Enrollment">
      
      <br> <br>
      
      <table>
        <tr>
          <th> ''' + year + ''' </th>
          <th> Status </th>
          <th> ECTS </th>
        </tr>
    ''')

def get_subjects():
    if year != "Enrollment":
      for key in subjects.subjects:
        if subjects.subjects[key].get("year") == subjects.year_ids[year]:
           print('''
           <tr>
             <td> ''' + subjects.subjects[key].get("name") + ''' </td>
             <td> ''' + str(subjects.subjects[key].get("ects")) + ''' </td>
             <td>
           ''')

           for status in subjects.status_names:
              if not all_cookies_object.get(key):
                print(subjects.status_names[status] + ' <input type="radio" name="' + key + '" value="' + subjects.status_names[status] + '">')
              elif all_cookies_object.get(key).value != subjects.status_names[status]:
                print(subjects.status_names[status] + ' <input type="radio" name="' + key + '" value="' + subjects.status_names[status] + '">')
              elif all_cookies_object.get(key).value == subjects.status_names[status]:
                print(subjects.status_names[status] + ' <input type="radio" name="' + key + '" value="' + subjects.status_names[status] + '" checked>')
        print('</td> </tr>')


    elif year == "Enrollment":
      total_ECTS = 0
      for key in subjects.subjects:
        if all_cookies_object.get(key):
           print('''
           <tr>
             <td> ''' + subjects.subjects[key].get("name") + ''' </td>
             <td> ''' + str(subjects.subjects[key].get("ects")) + ''' </td>
             <td> ''' + all_cookies_object.get(key).value + ''' </td>
           </tr>
           ''')
           if all_cookies_object.get(key).value == "Enrolled":
             total_ECTS += subjects.subjects[key].get("ects")
      print('''
      <tr>
        <td> <b>Total:</b> </td>
        <td> <b>''' + str(total_ECTS) + '''</b> </td>
        <td> <b>Enrolled</b> </td>
      </tr>
      ''')

base.start_html()
print_navigation()
get_subjects()
base.end_html()