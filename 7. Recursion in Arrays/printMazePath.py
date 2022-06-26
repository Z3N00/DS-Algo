def printMazePath(sr, sc, dr, dc, ans):

    if(sr==dr and sc == dc):
        print(ans)
        return
    if (sr>dr or sc>dc):
        return

    printMazePath(sr, sc+1, dr, dc, ans + "h")
    printMazePath(sr+1, sc, dr, dc, ans + "v")





printMazePath(1,1,3,3, "")