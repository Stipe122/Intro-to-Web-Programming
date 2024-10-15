#!python

import cgi
params = cgi.FieldStorage()

if(params.getvalue("password") != params.getvalue("password2")):
	print("Location: ./index.py\n\n");

print ("Content-type:text/html\r\n\r\n")
print ('''
<!DOCTYPE html>
<html>
<body>

		<form action="./index3.py" method="post">
			Status:
			<input
				type="radio"
				name="student_status"
				value="Redovan"
				checked
			/>Redovni
			<input
				type="radio"
				name="student_status"
				value="Izvanredan"
			/>Izvandredan<br />
			E-mail: <input type="email" name="email" value="" /><br />
			Smjer:<select name="smjer">
				<option value="programiranje">Programiranje</option>
				<option value="racunarstvo">Racunarstvo</option>
				<option value="elektrotehnika">Elektrotehnika</option>
				<option value="bazepodataka">Baze podataka</option>
			</select>

			Završni:
			<input type="checkbox" name="zavrsni_upisan" value="Da" checked /><br />

            
			<input type="submit" value="Next" /><br />
		''')

print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')

print ('''
</form> 

</body>
</html>''')

