
def noOfStep(n):

    if(n==0):
        return [""]
    elif(n<0):
        return []


    paths1 = noOfStep(n-1)    
    paths2 = noOfStep(n-2)
    paths3 = noOfStep(n-3)

    paths = []

    for path in paths1:
        paths.append("1"+ path)

    for path in paths2:
        paths.append("2"+ path)

    for path in paths3:
        paths.append("3" + path)


    return paths




n = int(input()) # number of staircases
res = noOfStep(n)
op = [int(i) for i in res]
print(op)