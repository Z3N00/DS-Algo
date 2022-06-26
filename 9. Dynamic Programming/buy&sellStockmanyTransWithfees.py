n = int(input())

arr = [int(input()) for i in range(n)]


fees = int(input())
obsp = -arr[0]
ossp = 0
for i in range(n):
    nbsp = 0
    nssp = 0

    if(ossp - arr[i] > obsp):
        nbsp = ossp - arr[i]
    else:
        nbsp = obsp
    if(obsp + arr[i] - fees > ossp):
        nssp = obsp + arr[i] - fees
    else:
        nssp = ossp

    obsp = nbsp
    ossp = nssp

print(ossp)