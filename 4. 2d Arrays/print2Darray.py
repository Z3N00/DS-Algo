n = 3
m = 4
arr = []


for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    arr.append(a)


for i in range(n):
    for j in range(m):

        print(arr[i][j], end = " ")

    print( )
