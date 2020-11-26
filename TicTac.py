#!/usr/bin/env python3

#Tic Tac Toe program by Supakjeera Thanapaisal for Plus One Robotic Technical Assessment process
#if you already have python and you are on linux: python3 TicTac.py
import random
import copy

#print function
def printFunc(board):
    for row in board:
        print(row)

#insert location
def insert(currBoard,loc,player):
    newLoc = loc % 3
    if loc in board[0]:
        currBoard[0][newLoc] = player
    elif loc in board[1]:
        currBoard[1][newLoc] = player
    elif loc in board[2]:
        currBoard[2][newLoc] = player


def checkIfWin(currBoard,player):

    #return True == win, False == not yet
    win = rowcolCheck(currBoard,player)
    if win:
        return win
    win = diagCheck(currBoard,player)
    if win:
        return win

    return win

def rowcolCheck(currBoard,player):
    
    #ROW
    flag = False
    #check if currplayer has the whole row for each of them
    for each in currBoard:
        if each.count(player) == len(currBoard):
            flag = True
            break
    if flag:
        return flag

    #COL
    for i in range(len(currBoard)):
        flag = True
        for j in range(len(currBoard)):
            if currBoard[j][i] != player:
                flag = False
                break
        if flag == True:
            return flag

    return flag


def diagCheck(currBoard,player):

    # check [0,0][1,1][2,2]
    flag = True
    for i in range(len(currBoard)):
        if currBoard[i][i] != player:
            flag = False
            break
    if flag:
        return flag
    
    # check [0,2][1,1][2,0]
    flag = True
    j = len(currBoard)-1
    for i in range(len(currBoard)):
        if currBoard[i][j] != player:
            flag = False
            break

        j -= 1
        
    return flag

#Beginning of the code 
#globals
board = [[0,1,2],
         [3,4,5],
         [6,7,8]]
choiceList = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8}
p1 = 'X'
p2 = 'O'

print("______________________________________")
print("Welcome to a simple Tic Tac Toe game!")
printFunc(board)
print("You: 'X'")
print("PC: 'O'")

try:
    #Every new game
    while True:

        status = int(input("Do you want to play? [Yes = 1,No = 2]: "))
        if status != 1:
            print("Thanks for playing :)")
            break
        currentBoard = copy.deepcopy(board)
        choices = choiceList.copy()
        printFunc(currentBoard)

        
        while status:
            #get uset's input
            print("______________________________________")
            p1Move = int(input("Insert the position on the board [0-8]: "))
            #check if the choice is valid
            if p1Move not in choices:
                print("Invalid location or already been inserted")
                continue
            #remove from availible choices 
            del choices[p1Move]
            #auto update because pointing to the same object board
            insert(currentBoard,p1Move,p1)

            #check if user wins
            if checkIfWin(currentBoard,p1):
                print("You won! Congrats")
                status = 0  
                continue
            # this is for the last round (9), determine if tie after checking if the player win
            if not choices:
                print("It's a tie! Try again")
                status = 0
                continue
            
            #computer's turn
            #get keys that has no value of -1 then pick random num from that list
            aval = [key for (key, value) in choices.items()]
            p2Move = random.choice(aval)
            del choices[p2Move]
            insert(currentBoard,p2Move,p2)

            #check if computer wins
            if checkIfWin(currentBoard,p2):
                print("You lost! Sorry :s")
                status = 0  
                continue

            printFunc(currentBoard)

except KeyboardInterrupt:
    print("Thanks for playing :)")
