import sqlite3 #import sqlite3 module/libary

"create a variable 'conn' and pass sqlite3.connect method to it"
#pass in folderpath/dbName.db as parameter,which will create the DB
# if it does not exist/ otherwise use it if it exist

conn = sqlite3.connect("PY/Week3/SQLite/c7Music.db")
cursor= conn.cursor()#cursor method iterates through database/tables
