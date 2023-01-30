"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX=0
    countO=0
    
    for i in board:
        for j in i:
            if j==X:
                countX+=1
            elif j==O:
                countO+=1
    if countX==5:
        return None
    elif countX==countO:
        return X
    elif countX>countO:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==EMPTY:
                moves.add((i,j))
    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard=copy.deepcopy(board)

    if player(newboard)==X:
        newboard[action[0]][action[1]]=X
        return newboard
    elif player(newboard)==O:
        newboard[action[0]][action[1]]=O
        return newboard
    else:
        raise NameError('Not a valid move')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==board[0][1]==board[0][2] and board[0][0]!=EMPTY:
        return board[0][0]
    elif board[1][0]==board[1][1]==board[1][2] and board[1][0]!=EMPTY:
        return board[1][0]
    elif board[2][0]==board[2][1]==board[2][2] and board[2][0]!=EMPTY:
        return board[2][0]
    elif board[0][0]==board[1][0]==board[2][0] and board[0][0]!=EMPTY:
        return board[0][0]
    elif board[1][1]==board[0][1]==board[2][1] and board[0][1]!=EMPTY:
        return board[0][1]
    elif board[1][2]==board[2][2]==board[0][2] and board[0][2]!=EMPTY:
        return board[0][2]
    elif board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        return board[0][0]
    elif board[2][0]==board[1][1]==board[0][2] and board[2][0]!=EMPTY:
        return board[2][0]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    elif player(board)==None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    maximove=[]
    minimove=[]
    def maxi(board):
        v=-2
        if terminal(board):
            return utility(board)
        for i in actions(board):
            v=max(v,mini(result(board,i)))
        return v
        
    def mini(board):
        v=2
        if terminal(board):
            return utility(board)
        for i in actions(board):
            v=min(v,maxi(result(board,i)))
        return v

    if player(board)==X:
        for i in actions(board):
            if mini(result(board,i))>=0:
                return i


    elif player(board)==O:
        for i in actions(board):
            if maxi(result(board,i))<=0:
                return i

    else:
        return None
