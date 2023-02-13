# Carter Belnap
# Feburary 7th 2023
# Battleship Program

import random,os

spot =["~"]*25

run=True
#Game Start

while run:
    ammo = 10
#Printing Board
    i=0
    row=1
    print("\n""Welcome To Battelship! Try To Sink My Ships!")
    print("\n" )
    print("  A B C D E")
    print("-----------")
    while i<25:
        print(f"{row} {spot[i]} {spot[i+1]} {spot[i+2]} {spot[i+3]} {spot[i+4]}")
        i+=5
        row+=1

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

    if spot[row + start_v]=="M":
        print("You Have Already Guessed Here")
    else:
        spot[row + start_v]= "M"
        ammo=-1
    
    if row>=6:
        print("Please Print A Valid Number")
   
        
    os.system("cls")        

        
shiprandom = random.randint(0,11) 
  
  
  #BOARD
  # 1 2 2 4 4 
  # 1 3 3 3 5
  # 7 7 6 6 5
  # 8 9  9  9  10
  # 8 11 11 11 10
  