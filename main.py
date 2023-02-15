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

  #Ship Placing
       
shiprandom = random.randint(0,11)
shiprandom2 = random.randint(0,11)
while shiprandom==shiprandom2:
    shiprandom2 = random.randint(0,11)
      
ships=["M "]*25
  
  #BOARD CARD
  # 1 2 2 4 4 
  # 1 3 3 3 5
  # 7 7 6 6 5
  # 8 9  9  9  10
  # 8 11 11 11 10
  
if shiprandom==1:
    ships[0] = "H "
    ships[5] = "H "
if shiprandom==2:
    ships[1] = "H "
    ships[2] = "H "
if shiprandom==3:
    ships[6] = "H "
    ships[7] = "H "
    ships[8] = "H "
if shiprandom==4:
    ships[3] = "H "
    ships[4] = "H "
if shiprandom==5:
    ships[9] = "H "
    ships[14] = "H "
if shiprandom==6:
    ships[12] = "H "
    ships[13] = "H "
if shiprandom==7:
    ships[10] = "H "
    ships[11] = "H "
if shiprandom==8:
    ships[15] = "H "
    ships[20] = "H "
if shiprandom==9:
    ships[16] = "H "
    ships[17] = "H "
    ships[18] = "H "
if shiprandom==10:
    ships[19] = "H "
    ships[24] = "H "
if shiprandom==11:
    ships[21] = "H "
    ships[22] = "H "
    ships[23] = "H "

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
    try:   
        guess=(input("Guess Where The Ships Are!:")).upper()
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
            print("Please Print A Valid Letter!")
            start_v=-1
        if not start_v==-1 and not int(guess[1])>5:
            if board[row + start_v]==ships[row + start_v]:
                print("You Have Already Guessed Here")
                time.sleep(2)
            else:
                board[row + start_v]= ships[row + start_v]
                
        else:
            print("Please Enter A Valid Number!")
            time.sleep(2)
            
        os.system("cls")  
    except:
            print("Please Enter A Valid Guess!")
            time.sleep(2)       

 