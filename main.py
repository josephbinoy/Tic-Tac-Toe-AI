from ai import *
from os import *

board=[' ',' ',' ',
       ' ',' ',' ',
       ' ',' ',' ']

def boardIsFull():
    for cell in board:
        if cell==' ':
            return False
    return True

def checkValidMove(board, move):
    if(board[move]!=' '):
        return False
    return True

def checkWinner(board):
    if(terminal(board)):
        system('cls')
        displayBoard(board)
        result=utility(board)
        if(result==1):
            return "Computer wins!"
        elif(result==-1):
            return "You win!" #impossible btw
        else:
            return "It's a draw"
    return False

def displayBoard(board):
    print('\n   ',board[0], '|', board[1], '|', board[2])
    print('   ---|---|---')
    print('   ',board[3], '|', board[4], '|', board[5])
    print('   ---|---|---')
    print('   ',board[6], '|', board[7], '|', board[8], '\n')

while not boardIsFull():
    system('cls')
    displayBoard(board)
    move=int(input("Enter the coordinates of your move: "))
    if not checkValidMove(board, move):
        print("Invald move")
        continue
    board[move]='O'
    if winner:=checkWinner(board):
        print(winner)
        break
    move=getComputerMove(board)
    board[move]='X'
    if winner:=checkWinner(board):
        print(winner)
        break




