
def NQueens(chess, qsf, row):

    if(row == len(chess)):
        print(qsf + ".")
        return

    for col in range(len(chess)):
        #print(isQueenSafe(chess, row, col))
        if(isQueenSafe(chess, row, col) == True):

            chess[row][col] = 1
            NQueens(chess, qsf + str(row) + "-" + str(col) + ", ", row+1)
            chess[row][col] = 0




def isQueenSafe(chess, row, col):

    # upward direction
    for i in range(row - 1, -1, -1):
        if(chess[i][col]==1):
            return False

    # diagonal left
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if(chess[i][j]==1):
            return False

    # diagonal right
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(chess))):
        if(chess[i][j]==1):
            return False

    return True
    

if __name__ == "__main__":
    n = 4
    chess = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        chess.append(a)
    

    NQueens(chess, "", 0)