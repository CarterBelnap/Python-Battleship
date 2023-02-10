# Carter Belnap
# Feburary 7th 2023
# Battleship Program

import random,os

spot =["*"]*25

run=True
#Game Start

while run:
    
#Printing Board
    i=0
    row=1

    print("  A B C D E")
    print("-----------")
    while i<25:
        print(f"{row} {spot[i]} {spot[i+1]} {spot[i+2]} {spot[i+3]} {spot[i+4]}")
        i+=5
        row+=1

        guess=(input("Guess Where The Ships Are!:"))
        letter=guess[0]
        row=(guess[1]-1)*5
        
        if letter=="A":
            start_v=0
        elif letter=="B":
            start_v=1
        elif letter=="C":
            start_v=2
        elif letter=="D":
            start_v=4
        elif letter=="E":
            start_v=5
        else letter=-1:
            print("Please Print A Valid Number")


    
        if spot[row + start_v]=="M":
            print("You Have Already Guessed Here")
        else:
            spot[guess]= "M"
        
    os.system("cls")        

        
    random_num = random.randint(0,25) 
  