n = int(input())

arr = [int(input()) for i in range(n)]


obsp = -arr[0]
ossp = 0
ocsp = 0

for i in range(len(n)):
    nbsp = 0
    nssp = 0
    ncsp = 0

    if(ocsp - arr[i] > obsp):
        nbsp = ocsp - arr[i]
    else:
        nbsp = obsp

    if(obsp + arr[i] > ossp):
        nssp = obsp + arr[i]
    else:
        nssp = ossp
    if(ossp > ocsp):
        ncsp = ossp
    else:
        ncsp = ocsp

    obsp = nbsp
    ocsp = ncsp
    ossp = nssp

    print(ossp)