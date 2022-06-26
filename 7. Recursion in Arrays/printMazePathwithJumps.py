def printMazeWithJumps(sr, sc, dr, dc, ans):

    if(sr==dr and sc == dc):
        print(ans)
        return

    for ms in range(1, dc-sc+1):
        printMazeWithJumps(sr, sc+ms, dr, dc, ans + "h" + str(ms))

    for ms in range(1, dr-sr+1):
        printMazeWithJumps(sr+ms, sc, dr, dc, ans + "v" + str(ms))

    ms = 0
    while((ms <= dr-sr) and (ms <= dc-sc)):
        ms += 1
        printMazeWithJumps(sr+ms, sc+ms, dr, dc, ans + "d" + str(ms))
    


printMazeWithJumps(1,1,3,3,"")