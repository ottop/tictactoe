square=[" "," "," "," "," "," "," "," "," "] #A list for the squares which are empty at this point
win=[[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]] #A list of win condition lists

players=["",""] #A list of the 2 players

def wincheck(): #Function to check if a win condition is met
    for i in range(0,8):
        if square[win[i][0]-1]==square[win[i][1]-1]==square[win[i][2]-1] and square[win[i][2]-1]!=" ": #If all the squares within a win condition are the same and not empty
            print(square[win[i][0]-1],"wins")
            import sys
            exit()
            
while True: #Asks for who starts until the answer is either x or o
    players[0]=input("Who starts (x or o)?")
    if players[0]=="x":
        players[1]="o"
        break
    elif players[0]=="o":
        players[1]="x"
        break
    else: print("You need to enter either x or o")

def squares(): #The function that goes through the gameplay itself
    turn=1
    while True: 
        draw()
        turn+=1
        wincheck()
        if turn>10: #Ends the game in a draw if all squares are taken and nobody has won
            print("It's a draw")
            exit()
        try: #If answer to squareno is an integer
            squareno=int(input(str(players[turn%2])+", enter the number of the square you wish to take: "))
            if square[squareno-1]==" ":
                square[squareno-1]=players[turn%2]
            else:
                print("Please pick a square between 1 and 9 that is not occupied")
                turn-=1
        except: #If the answer is not an integer
            print("\nYour input needs to be an integer of a free square between 1 and 9")
            turn-=1

def draw(): #Defines the function to draw the grid
  print("")
  for i in range(0, 3):
    print("    " + str(1 + i * 3) + "     " + str(2 + i * 3) + "     " + str(3 + i * 3)+"\n"+" |  " + str(square[0 + i * 3]) + "  |  " + str(square[1 + i * 3]) + "  |  " + str(square[2 + i * 3]) + "  | ")

squares()
