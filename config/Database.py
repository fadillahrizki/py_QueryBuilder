import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="py_basic"
)

cursor = database.cursor()