from ast import Delete
from dbConnect import *
import readSongs
import time

def deleteSong():
    #songID to be deleted
    idField = input("Enter the SongID of the song you want to delete: ")
        #DELETE FROM SONGS WHERE songID 1 = songID(1) entered by the user
    cursor.execute("DELETE FROM songs WHERE SongID=" + idField)#songID(4) =4
    conn.commit()

    print(f"Record {idField} deleted")
    time.sleep(3)
    readSongs.read()#invoke/callung readSongs from the readSong python

    # o check if record exist
    #try except or use an if statement
    #if songid != idField
    #print(The is no match for that record or id )
    #else:
    #cursor.execute("DELETE FROM songs WHERE SongID=" + idField)

#deleteSong()