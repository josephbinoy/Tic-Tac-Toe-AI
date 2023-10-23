#the minimax function. It starts the recursive chain, calling minvalue and maxvalue alternatively till leaf node reached and returns the index of the best move.
#why minvalue first? 
#computer is the 'max' player, human is the 'min' player. So it needs to calculate the maximum score from its children
#and since the children represent human's move, we need to calculate minimum score of the children's children (computer's granchildren).
#again the grandchildren will need to calculate maximum score of THEIR children as its the computer's turn then.
#this chain continues till leaf node is reached
def getComputerMove(board):
    actionList=actions(board)
    bestValue=-9999
    bestCost=-9999
    for a in actionList:
        childValue, cost=minValue(result(board,a), 0)
        if bestValue < childValue:
            bestValue, bestCost=childValue, cost
            i=a[1]
        elif bestValue==childValue:
            if bestCost>cost:
                bestValue=childValue
                bestCost=cost
                i=a[1]
    return i

#function that evaluates given position and returns a score: 1 for X win, -1 for O win, 0 for draw. 
#it is guaranteed that this function will be called only in terminal positions.
def utility(board):
    #check rows
    for row in range(0,8,3):
        if board[row]==board[row+1]==board[row+2]!=' ':
            if board[row]=='X':
                return 1
            elif board[row]=='O':
                return -1
    
    #check columns
    for col in range(0,3):
        if board[col]==board[col+3]==board[col+6]!=' ':
            if board[col]=='X':
                return 1
            elif board[col]=='O':
                return -1
    
    #check diagonals
    if (board[0]==board[4]==board[8]!=' ') or (board[2]==board[4]==board[6]!=' '):
        if board[4]=='X':
            return 1 
        elif board[4]=='O':
            return -1
    #draw
    return 0

#function that returns a new board given current board and move to be played
def result(board, action):
    (player, index) = action
    newBoard=board.copy()
    newBoard[index] = player
    return newBoard

#function that returns the value of the child with lowest utility score along with its depth/cost (lower is better)
def minValue(board, cost):
    if terminal(board):
        return (utility(board),cost)
    
    score=9999
    actionList=actions(board)
    for a in actionList:
        v, c=maxValue(result(board,a), cost+1);
        if  score > v:
            score=v
            cost=c
        elif score==v:
            score=v
            cost=min(c, cost)
    return (score, cost)

#function that returns the value of the child with highest utility score along with its depth/cost (lower is better)
def maxValue(board, cost):
    if terminal(board):
        return (utility(board),cost)
    
    score=-9999
    actionList=actions(board)
    for a in actionList:
        v, c=minValue(result(board,a), cost+1);
        if  score < v:
            score=v
            cost=c
        elif score==v:
            score=v
            cost=min(c, cost)
    return (score, cost)

#function that checks if game is over
def terminal(board):
    #check rows
    for row in range(0,8,3):
        if board[row]==board[row+1]==board[row+2]!=' ':
            return True
    
    #check columns
    for col in range(0,3):
        if board[col]==board[col+3]==board[col+6]!=' ':
            return True
    
    #check diagonals
    if (board[0]==board[4]==board[8]!=' ') or (board[2]==board[4]==board[6]!=' '):
        return True

    #check if draw
    for cell in board:
        if(cell == ' '):
            break
    else:
        return True

    #game not over
    return False
    

#function that returns all allowed moves in given position in the form (player_name, board_index)
def actions(board):
    player=getPlayer(board)
    allowedMovesList=[]
    i=0
    while(i<9):
        if board[i]==' ':
            allowedMovesList.append((player,i))
        i+=1
    return allowedMovesList

#function that returns the player whose turn is next in the given board
def getPlayer(board):
    xCount=0
    oCount=0
    for cell in board:
        if cell=='X':
            xCount+=1
        elif cell=='O':
            oCount+=1
    if(xCount+oCount==9):
        return None
    if(xCount<oCount):
        return 'X'
    else:
        return 'O'
