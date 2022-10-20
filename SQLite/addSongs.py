from dbConnect import * 
import time

# create a subroutine to add songs to the songs table in the c7Music.db 
def addSongs():
    # create an empty list
    songs = []
# start of while loop
    # songID field is autoIncrement 

    #capture data inputted from the user
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    genre = input("Enter song genre: ")

    # append the dat captured from user
    # songs.songID is auto increment and would be added automatically
    songs.append(title)
    songs.append(artist)
    songs.append(genre)
    

    # insert data into songs table in c7Music.db 
    cursor.execute("INSERT INTO songs VALUES(NULL,?,?,?) ", songs)
    conn.commit() # commiing the chnages
    print(f"{title} added to Songs Table") # print out the song added
    time.sleep(3) # delay for 3 seconds before executing the select statement below
# end of while loop
    # read data from table songs in c7Music.db 
    cursor.execute("SELECT * FROM songs") # select all songs
    row = cursor.fetchall() # use to fetch all data from the songs table and pass it to variable "row"
    for record in row:
        print(record)

#addSongs() # call/invoke the function
