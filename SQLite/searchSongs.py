from dbConnect import *
import time

def search():
    #enter the name of the field to search
    searchfield = input("Which field value would you like to search: ").title()
    #enter the value of the fieldName to be updated
    searchValue = input(f"Enter the value for the {searchfield} you want to search").capitalize()
    print(f"The field value entered by the user is {searchValue} ")

    searchValue = "'" + searchValue + "'"
    print(f"Amended search value {searchValue} ")

    cursor.execute("SELECT * FROM songs WHERE " + searchfield + "=" + searchValue)
    conn.commit()

    time.sleep(3)
    row = cursor.fetchall()
    strRow = str(row)
    if searchValue in strRow:#.title()
        for record in row:
            print(record)
    else:
        print(f"The field {searchfield} does not contain a {searchValue} in the database!")
    #conn.close()
#search()