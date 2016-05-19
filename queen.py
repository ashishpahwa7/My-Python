import numpy as np

def isColumnSafe(chessboard, N, col):
    
    
    for i in range(0, N):
        if chessboard[i][col] :
            return 0
    return 1

def isRowSafe(chessboard, N, row):

    for i in range(0, N):
        if chessboard[row][i] :
            return 0
    return 1


def isDiagonalSafe(chessboard, N, row, col):

    """Check left upper diagnol"""

    i = row
    j= col

    while( ( i >= 0 and j >= 0 ) or ( i == row and j == col ) ):

        if (chessboard[i,j]):

            return 0

        i = i-1
        j = j-1

    
    
    """Check left lower diagnol"""

    i=row
    j=col

    while( ( i < N and j < N ) or ( i == row and j== col ) ):

        if( chessboard[i,j] ):
            return 0

        i=i+1
        j=j+1

    
    """Check right upper diagnol"""

    i=row
    j=col

    while( ( i >= 0 and j < N ) or ( i == row and j== col ) ):

        if(chessboard[i,j]):
            return 0
        i=i-1
        j=j+1

    """Check right lower diagnol"""

    i=row
    j=col

    while( ( i < N and j >= 0 ) or ( i == row and j== col ) ):

        if(chessboard[i,j]):
            return 0
        i=i+1
        j=j-1

    
    return 1


def isPlaceSafe(chessboard, N, row, col):

    colSafe = isColumnSafe(chessboard, N, col)
    rowSafe = isRowSafe(chessboard, N, row)
    diagonalSafe = isDiagonalSafe(chessboard, N, row, col)

    return colSafe and rowSafe and diagonalSafe


def placeQueen(chessboard, i, j):

    chessboard[i][j] = 1





def removeQueen(chessboard, i, j):

    chessboard[i][j] = 0



def solveQueen(chessboard, N, col):

    if(col >= N):
        return 1

    for i in range(0,N):
        if( isPlaceSafe(chessboard, N, i, col)):
            placeQueen(chessboard, i, col)

            if( solveQueen(chessboard, N, col+1)):
                return 1

            removeQueen(chessboard, i, col)






chessboard = np.zeros((8,8),dtype=np.int)
N=8
col=0
solveQueen(chessboard, N, col)
print(chessboard)









































