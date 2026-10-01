from getpass import getpass
from pysql_init import userDB
import os
import hashlib

SQL = userDB.cursor()

def signUp():
    email = input("Enter email address: ")
    pwd = getpass("Enter password: ")
    conf_pwd = getpass("Confirm password: ")

    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hashedPwd = hashlib.md5(enc).hexdigest()

        SQL.execute("INSERT INTO userInfo (Email, Password) VALUES ('"+email+"', '"+hashedPwd+"');")
        userDB.commit()
        print("You have registered succesfully")

    else:
        print("Password is not the same as above!")

def signIn(inputFunction):
    email = input("Enter email address: ")
    pwd = getpass("Enter password: ")

    enc = pwd.encode()
    hashedPwd = hashlib.md5(enc).hexdigest()

    SQL.execute("SELECT * FROM userInfo WHERE Email = %s AND Password = %s;", (email, hashedPwd))

    if SQL.fetchall():
        print("Login Successful!")
        inputFunction()
    else:
        print("Login Failed")

print ('1. Sign Up')