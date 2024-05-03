import sqlite3
import hashlib

connection =  sqlite3.connect("userdata.db")

cur = connection.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
)


""")


username1, pass1= "ian123", hashlib.sha256("ianpass1".encode()).hexdigest()
username2, pass2= "ian234", hashlib.sha256("ianpass2".encode()).hexdigest()
username3, pass3= "ian345", hashlib.sha256("ianpass3".encode()).hexdigest()
username4, pass4= "ian456", hashlib.sha256("ianpass4".encode()).hexdigest()


cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username1,pass1))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username2,pass2))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username3,pass3))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username4,pass4))


connection.commit()