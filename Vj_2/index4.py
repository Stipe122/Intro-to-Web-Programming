#!python

import cgi
params = cgi.FieldStorage()

print ("Content-type:text/html\r\n\r\n")
print ('''
<!DOCTYPE html>
<html>
<body>
        <a href="index.py">Na pocetak</a>
		<form action="./index.py" method="post">
            <h2>Uneseni podaci</h2><br />''')
print ('Ime: <input type="text" name="firstname" value="' + params.getvalue("firstname") + '"><br />')
print ('E-mail: <input type="text" name="email" value="' + params.getvalue("email") + '"><br />')
print ('Status: <input type="text" name="status" value="' + params.getvalue("status") + '"><br />')
print ('Smjer: <input type="text" name="smjer" value="' + params.getvalue("smjer") + '"><br />')
print ('Završni rad: <input type="text" name="zavrsni_rad" value="' + params.getvalue("zavrsni_rad") + '"><br />')
print ('Napomene: <input type="text" name="napomenaValue" value="' + params.getvalue("napomene") + '"><br />')






print ('''<br><br>
</form> 

</body>
</html>''')

