from readSongs import *
from addSongs import *
from searchSongs import *
from updateSongs import *
from delete import *


#create a function for the menu
def menuOptions():
    options = 0 #a flag variable otions =0
    # check for the variable options which has a value set to zero "0"
    while options not in ["1", "2", "3", "4", "5", "6"]:
        print("\Menu Options\n1. Print Songs.\n2. Add Songs.\n3. Update Songs.\n4. Search Songs\n5. Delete Songs\n6. Exit ")
        #reset the value for the option variable and assign it a new value
        options = input("\n Enter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not in a option value")
    return options

mainProgram = True

while mainProgram == True:
    #pass menuOption() function to the variable main Menu 
    mainMenu = menuOptions()
    if mainMenu == "1":
        read()
    elif mainMenu == "2":
        addSongs()
    elif mainMenu == "3":
        update()
    elif mainMenu == "4":
        search()
    elif mainMenu == "5":
        deleteSong()
    else:
        mainProgram = False
input("Press enter to exit")



         