# Carter Belnap
# Feburary 7th 2023
# Battleship Program

#Imports
import random,os,time
#Game Start
run=True
e=1
board=[]
#Board Printing
while e<=25:
    board.append("A"+str(e))
    board.append("B"+str(e))
    board.append("C"+str(e))
    board.append("D"+str(e))
    board.append("E"+str(e))
    e+=1

while run:
   
#Board/UI Printing
    i=0
    row=1 
    ammo = 10
    print("\n""Welcome To Battelship! Try To Sink My Ships!")
    print("\n" )
    print("  A  B  C  D  E ")
    print("----------------")
    while i<25:
        print(f"{row} {board[i]} {board[i+1]} {board[i+2]} {board[i+3]} {board[i+4]}")
        i+=5
        row+=1

#ASCII Guessing UI
    print(f"Ammo = {ammo}")
    guess=(input("Guess Where The Ships Are!:"))
    letter=guess[0]
    row=(int(guess[1])-1)*5
    
    if letter=="A":
        start_v=0
    elif letter=="B":
        start_v=1
    elif letter=="C":
        start_v=2
    elif letter=="D":
        start_v=3
    elif letter=="E":
        start_v=4
    else:
        print("Please Print A Valid Letter")
        start_v=-1
    if not start_v==-1 and not int(guess[1])>5:
        if board[row + start_v]=="M ":
            print("You Have Already Guessed Here")
        else:
            board[row + start_v]= "M "
            
    else:
        print("Please Enter A Valid Number!")
        time.sleep(2)
        
    os.system("cls")        

        
shiprandom = random.randint(0,11) 
  
  #BOARD CARD
  # 1 2 2 4 4 
  # 1 3 3 3 5
  # 7 7 6 6 5
  # 8 9  9  9  10
  # 8 11 11 11 10
  