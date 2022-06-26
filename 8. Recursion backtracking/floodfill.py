
def floodFill(maze, row, col, psf, visited):
    print("function call pass")
    if(row<0 or col<0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 1 or visited[row][col] == True ):
        print("first return")
        return
    elif(row == len(maze)-1 and col == len(maze[0]-1)):
        print("printing answer")
        print(psf)
        return

    visited[row][col] = True
    print("visited true")
    # top
    floodFill(maze, row-1, col, psf + "t", visited)
    # left
    floodFill(maze, row, col-1, psf + "l", visited)
    # down
    floodFill(maze, row+1, col, psf + "d", visited)
    # right
    floodFill(maze, row, col+1, psf + "r", visited)
    visited[row][col] = False



row = 3 #int(input())
col = 3 #int(input())
maze = [[0,0,0],[1,0,1],[0,0,0]]
# for i in range(row):
#     a = []
#     for j in range(col):
#         a.append(int(input()))
#     maze.append(a)

visited = [[False] * col] * row

floodFill(maze, 0, 0,  "", visited)


