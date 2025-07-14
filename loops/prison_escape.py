"""
A text based game where we have to escape the prison. We will have some rooms like cells, halls, guard room and exit.
We have two choices- Left and Right. 
Starts in cell 0
Based on choices, they:
-Progress to the next room
-Get caught by a guard
-Trigger a trap and go back
-OR die 

I'll need- for loop, while loop, break, continue and list to store the map.
"""
#Lets get started! 
print("WELCOME TO THE PRISON ESCAPE")

list = ["cell-0", "cell-1", "cell-2", "hallway", "guard room", "exit"]
current_room = "cell-0"
start = input("Press ENTER to start the game. \n")

if start == "":
    print("You are currently in cell-0.")
else :
    print("You don't want to play? Get lost.")
    exit()



while True :

 move = input("Left or Right? Or wait..?\n").capitalize().strip()

 if move == "exit":
    print("Congratulations!! You have escaped the prison.")
    break 
 elif move == "":
    print("You have entered cell-2. Left or right?")
 elif move == "Wait":
    print("You see a door ahead. It leads to hallway. Wanna go?")
 else:
    while current_room!= "exit":
       move = input("Left or Right? Or...wait?\n")
       if move == "exitgame":
        print("You bailed like a coward. Game over.")
        break
 



