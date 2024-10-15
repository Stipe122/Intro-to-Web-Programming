#!python.exe
import mysql.connector  # pip install mysql-connector
import json
import password_utils
import itertools

db_conf = {
    "host": "localhost",
    "db_name": "subjects",
    "user": "root",
    "passwd": ""
}


def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb


def getSubjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM subjects"
    cursor.execute(
        query)
    myresult = cursor.fetchall()
    return myresult


def create_session(id):
    query = "INSERT INTO sessions (data) VALUES(%s)"
    values = (str(id))
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


# def get_session(session_id):
#     mydb = get_DB_connection()
#     cursor = mydb.cursor()
#     cursor.execute(
#         "SELECT * FROM sessions WHERE session_id=" + str(session_id))
#     myresult = cursor.fetchone()
#     return myresult[0], json.loads(myresult[1])

# replace - prvo izbrisi, a onda ubaci (delete/insert)


def replace_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data)
    VALUES (%s,%s)""",
                   (session_id, json.dumps(data)))
    mydb.commit()


def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

# Upisni list


def fillUpisniList(userId, id_predmeta, status):
    query = "INSERT INTO upisni_list (id_studenta, id_predmeta, status) VALUES(%s,%s,%s)"
    values = (userId, id_predmeta, status)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


def upisniListFromUserId(userId):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM upisni_list WHERE id_studenta='" + str(userId) + "'")
    myresult = cursor.fetchall()
    return myresult


def getSubjectNameForListById(predmetId):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM subjects WHERE id='" + str(predmetId) + "'")
    myresult = cursor.fetchall()
    return myresult[0]


def getSubjectIdFromListByName(name):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT id FROM subjects WHERE kod='" + str(name) + "'")
    myresult = cursor.fetchone()
    return myresult[0]


def getStatusByUserIdAndPredmetId(idPredmeta, idUser):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT status FROM upisni_list WHERE id_studenta='" + str(idUser) + "'" + "AND id_predmeta='" + str(idPredmeta) + "'")
    myresult = cursor.fetchone()
    return myresult[0]


def changeUserListByPredmetId(userId, predmetId, newValue):
    query = "UPDATE upisni_list SET status=%s WHERE id_studenta=%s AND id_predmeta=%s"
    values = (str(newValue), userId, predmetId)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


# Authentication


def checkName(params):
    name = params.getvalue("name")
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE ime='" + str(name) + "'")
    myresult = cursor.fetchone()
    return myresult


def getUserId(name):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE ime='" + str(name) + "'")
    myresult = cursor.fetchone()
    return myresult


def checkUsername(params):
    name = params.getvalue("username")
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE ime='" + str(name) + "'")
    myresult = cursor.fetchone()
    return myresult


def checkPassword(params):
    name = params.getvalue("username")
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE ime='" + str(name) + "'")
    myresult = cursor.fetchone()
    return myresult


def checkPasswordForReset(params):
    email = params.getvalue("email")
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE email='" + str(email) + "'")
    myresult = cursor.fetchone()
    return myresult


def checkEmail(params):
    email = params.getvalue("email")
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE email='" + str(email) + "'")
    myresult = cursor.fetchone()
    return myresult


def registerUser(params):
    ime = str(params.getvalue("name"))
    email = str(params.getvalue("email"))
    password = str(params.getvalue("password"))
    # Hash password
    hashPassword = password_utils.hash_password(password)
    query = "INSERT INTO users (ime, email, password) VALUES(%s,%s,%s)"
    values = (ime, email, hashPassword)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


def resetUserPassword(params, ime):
    email = str(params.getvalue("email"))
    password = str(params.getvalue("password"))
    # Hash password
    hashPassword = password_utils.hash_password(password)
    query = "REPLACE INTO users (ime, email, password) VALUES(%s,%s,%s)"
    values = (ime, email, hashPassword)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


# User roles

def get_user_role_enum(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT uloga FROM users WHERE id='" + str(user_id) + "'"
    cursor.execute(query)
    myres = cursor.fetchone()
    return myres[0]


def getAllUsers():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT ime FROM users WHERE uloga = 'student'")
    myresult = cursor.fetchall()
    return myresult
