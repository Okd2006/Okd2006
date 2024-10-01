#TIC TAC TOE GAME

#Displaying the board

board=["#",' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board():
    print("Welcome to the Tic Tac TOe game")
    print("    |     |")
    print(board[7],"  | ",board[8]," |  ",board[9])
    print("    |     |")
    print("----------------")
    print("    |     |")
    print(board[4],"  | ",board[5]," |  ",board[6])
    print("    |     |")
    print("----------------")
    print("    |     |")
    print(board[1],"  | ",board[2]," |  ",board[3])
    print("    |     |")

print("The rules of the game are very simple")
print("The X player goes first and then the O player")
print("Players have to choose the position of there move based on the numpad of the keyboard")

#Entering player input

def players_chance():
    while True:
        player_1=int(input("Enter your move (X):"))
        if player_1 in [1,2,3,4,5,6,7,8,9]:
            board[player_1]="X"  
        else:
            print("Please enter valid input")
            player_1=int(input("Enter your move (X):"))
        display_board()

        player_2=int(input("Enter yout move(O)"))
        if player_2 in [1,2,3,4,5,6,7,8,9]:
            board[player_2]="O"
        else:
            print("Please enter a valid input")
            player_2=int(input("Enter yout move(O)"))
        display_board()
        

def win1():
    win=True
    if board[7] and board[4] and board[1]=="X":
        print("Player 1 won")
        win=True
    elif board[8] and board[5] and board[2]=="X":
        print("Player 1 won")
        win=True
    elif board[9] and board[6] and board[3]=="X":
        print("Player 1 won")
        win=True
    elif board[7] and board[8] and board[9]=="X":
        print("Player 1 won")
        win=True
    elif board[4] and board[5] and board[6]=="X":
        print("Player 1 won")
        win=True
    elif board[1] and board[2] and board[3]=="X":
        print("Player 1 won")
        win=True
    elif board[7] and board[5] and board[3]=="X":
        print("Player 1 won")
        win=True
    elif board[1] and board[5] and board[9]=="X":
        print("Player 1 won")
        win=True
    elif board[7] and board[4] and board[1]=="O":
        print("Player 2 won")
        win=True
    elif board[8] and board[5] and board[2]=="O":
        print("Player 2 won")
        win=True
    elif board[9] and board[6] and board[3]=="O":
        print("Player 2 won")
        win=True
    elif board[7] and board[8] and board[9]=="O":
        print("Player 2 won")
        win=True
    elif board[4] and board[5] and board[6]=="O":
        print("Player 2 won")
        win=True
    elif board[1] and board[2] and board[3]=="O":
        print("Player 2 won")
        win=True
    elif board[7] and board[5] and board[3]=="O":
        print("Player 2 won")
        win=True
    elif board[1] and board[5] and board[9]=="O":
        print("Player 2 won")
        win=True

    def end():
        end=input("Do you want to continue : ")
        if end=="N":
            win=True
        while win is not True:
            break
        if win is True:
            pass
                  

            

        
            
                

    players_chance()
    win1()
    end()

        

    







    
    



        




   