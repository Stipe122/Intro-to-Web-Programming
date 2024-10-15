#!python

import cgi
params = cgi.FieldStorage()

print ("Content-type:text/html\r\n\r\n")
print ('''
<!DOCTYPE html>
<html>
<body>

		<form action="./index4.py" method="post">
			Napomene: <textarea name="napomene" row="5" cols="4"> </textarea><br />

			<input type="submit" value="Next" /><br />
		''')
print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')
print ('<input type="hidden" name="email" value="' + params.getvalue("email") + '">')
print ('<input type="hidden" name="status" value="' + params.getvalue("student_status") + '">')
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
print ('<input type="hidden" name="zavrsni_rad" value="' + params.getvalue("zavrsni_upisan") + '">')




print ('''
</form> 

</body>
</html>''')