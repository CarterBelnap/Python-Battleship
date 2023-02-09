# Carter Belnap
# Feburary 7th 2023
# Battleship Program

import random
spot =["*"]*25

run=True
while run:
    i=0
    row=1
    print("  A B C D E")
    print("-----------")
    while i<25:
        print(f"{row} {spot[i]} {spot[i+1]} {spot[i+2]} {spot[i+3]} {spot[i+4]}")
        i+=5
        row+=1
    guess=int(input("Guess Where The Ships Are!:"))
  
    if spot[guess]=="M":
        print("You Have Already Guessed Here")
    else:
          spot[guess]= "M"
          
    if spot[guess]>=25:
        print("PLEASE ENTER A VALID NUMBER \n IN THE BOX")     
        
    random_num = random.randint(0,25) 
    
    if random_num==
        print()
    