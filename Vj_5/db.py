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


def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid


def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

# replace - prvo izbrisi, a onda ubaci (delete/insert)


def replace_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
                   (session_id, json.dumps(data)))
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
