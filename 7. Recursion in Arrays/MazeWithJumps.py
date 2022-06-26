def MazeJump(sr, sc, dr, dc):


    if(sc == dc and sr == dr):
        return [""]
        
    paths = []

    # horizontal
    for ms in range(1, dc-sc+1):
        hpaths = MazeJump(sr, sc + ms, dr, dc)
        for hpath in hpaths:
            paths.append("h" + str(ms) + hpath)

    # Vertical
    for ms in range(1, dr-sr+1):
        vpaths = MazeJump(sr + ms, sc, dr, dc)
        for vpath in vpaths:
            paths.append("v" + str(ms) + vpath)

    # diagonal
    ms = 1
    while((ms <= dr-sr) and (ms <= dc-sc)):
        dpaths = MazeJump(sr + ms, sc + ms, dr, dc)
        for dpath in dpaths:
            paths.append("d" + str(ms) + dpath)
        ms += 1


    return paths



# n = int(input())
# m = int(input())
print(MazeJump(1,1,3,3))









