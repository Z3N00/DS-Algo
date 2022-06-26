def knightTour(chess, n, row, col, upcomingMove):
    
    if(row<0 or col<0 or row>=n or col>=n or chess[row][col]>0):
        return
    elif(upcomingMove == n*n):
        chess[row][col] = upcomingMove
        displayBoard(chess)
        chess[row][col] = 0
        return
    
    chess[row][col] = upcomingMove
    knightTour(chess, n, row-2, col+1, upcomingMove+1)
    knightTour(chess, n, row-1, col+2, upcomingMove+1)
    knightTour(chess, n, row+1, col+2, upcomingMove+1)
    knightTour(chess, n, row+2, col+1, upcomingMove+1)
    knightTour(chess, n, row-1, col+2, upcomingMove+1)
    knightTour(chess, n, row+2, col-1, upcomingMove+1)
    knightTour(chess, n, row+1, col-2, upcomingMove+1)
    knightTour(chess, n, row-1, col-2, upcomingMove+1)
    knightTour(chess, n, row-2, col-1, upcomingMove+1)
    chess[row][col] = 0

def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j], "", end = "")

        print()
    print()


if __name__ == "__main__":
    n = 5
    chess = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        chess.append(a)
    row = int(input())
    col = int(input())
    knightTour(chess, n, row, col, 1)