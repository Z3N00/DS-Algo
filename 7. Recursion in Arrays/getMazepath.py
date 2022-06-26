
def mazePath(sr, sc, dr, dc):
    
    if(sr>dr or sc>dc):
        return []
    elif(sr == dr and sc == dc):
        return [""]
    

    hpaths = mazePath(sr, sc+1, dr, dc)
    
    vpaths = mazePath(sr+1, sc, dr, dc)

    paths = []

    
    for hpath in hpaths:
        paths.append("h" + hpath)

    for vpath in vpaths:
        paths.append("v" + vpath)


    return paths

sr = 1
sc = 1
# n = int(input())
# m = int(input())

print(mazePath(sr, sc, 3, 3))