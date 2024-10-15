#!python

import cgi
params = cgi.FieldStorage()

print ("Content-type:text/html\r\n\r\n")
print ('''
<!DOCTYPE html>
<html>
<body>

		<form action="./index2.py" method="post">
			Ime: <input type="text" name="firstname" value="" /><br />
			Lozinka: <input type="password" name="password" value="" /><br />
			Ponovi lozinku:
			<input type="password" name="password2" value="" /><br />

			<input type="submit" value="Next" /><br />
		''')

print ('''<br><br>
</form> 

</body>
</html>''')



