import os
import random
def display_board(board):
    os.system("cls")
    print("    |   |")
    print("  "+ board[7] +" | "+ board[8] +" | "+ board[9])
    print("    |   |")
    print("--------------")
    print("    |   |")
    print("  "+ board[4] +" | "+ board[5] +" | "+ board[6])
    print("    |   |")
    print("--------------")
    print("    |   |")
    print("  "+ board[1] +" | "+ board[2] +" | "+ board[3])
    print("    |   |")

""" testboard=["#",'X','O','X','O','X','O','X','O','X']
display_board(testboard) """

def player_input():
    marker=''
    if(marker!="X" or marker!="O"):
        marker= input("Player 1, choose X or O: ").upper()
    player1=marker
    if player1=="X":
        return ("X","O") 
    else:
        return ("O","X") 
          
""" player_input()  """    

def place_marker(board,marker,position):
    board[position]=marker
""" place_marker(testboard,"$",8)    
display_board(testboard) """

def win_check(board,mark):
    if((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or
    (board[7]==board[8]==board[9]==mark) or (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or (board[7]==board[5]==board[3]==mark)):
        return True

""" display_board(testboard)
win_check(testboard,"X" ) """

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "Player 1"
    else:
        return "Player 2"   

def space_check(board,position):
    if board[position]==" ":
        return True

def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):   #if spacecheck is true
            return False            #board is not full
    return True                #board full

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose a position: (1-9)"))
    return position       

def replay():
    choice= input("Play again? Enter yes or no")
    return choice=="yes"    #if want to play yes is returned otherwise dont want to play

print("Welcome to TIK TAC TOE!!")
while True:                  #play the game
    the_board= [" "]*10
    player1_marker,player2_marker= player_input()
    turn= choose_first()
    print(turn + "will go first")

    play_game= input("Ready to play?  y or n :  ")
    if play_game=="y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":        #player1 turn
            display_board(the_board)                                  #show the board
            position = player_choice(the_board)                       #choose marker 
            place_marker(the_board,player1_marker,position)           #place marker
            if win_check(the_board,player1_marker):                    #check if won
                display_board(the_board)
                print("Player1 has won")
                game_on = False                                                 
            else:                                                       #check if tie
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                    break
                else:
                    turn = "Player 2"                      #no tie, no win, next players turn
                                        
        else:                                                   #player2 turn    
            display_board(the_board)                                  #show the board
            position = player_choice(the_board)                       #choose marker 
            place_marker(the_board,player2_marker,position)           #place marker
            if win_check(the_board,player2_marker):                    #check if won
                display_board(the_board)
                print("Player2 has won")
                game_on = False                                                 
            else:                                                       #check if tie
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                    break
                else:
                    turn = "Player 1"  
    if not replay():            #break out while loop
        break