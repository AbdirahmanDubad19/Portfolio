import readSongs
from dbConnect import * 
import time

def update():
    #songID to be updated
    idField = input("Enter the SongID of the song you want to be updated: ")
    #enter the name of the field to update
    fieldName = input("Which field value would you like to update:(Title, Artist, Genre) ").title()
    #enter the value of the fieldName to be updated
    newFieldValue = input(f"Enter the value for the {fieldName}")
    print(f"The field value entered by the user is {newFieldValue}")

    #add single quote to the value entered by the user
    newFieldValue = "'" + newFieldValue + "'" 
    print(f"The field value with single quotes added is {newFieldValue}")

    #UPDATE songs set the field to fieldName(user entry) with value = newFieldValue("my record") where songId(4) = idField
    cursor.execute("UPDATE songs SET " + fieldName + "=" + newFieldValue + "WHERE SongID = " + idField)
    conn.commit()
    print(f"Record {idField} Updated")
    time.sleep(3)
    readSongs.readSongs()


#update()