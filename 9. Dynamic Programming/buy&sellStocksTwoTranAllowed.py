n = int(input())

arr = [int(input()) for i in range(n)]

mpist = 0
leastsf = arr[0]
dpl = [0]*n
for i in range(1, n):
    if(arr[i] <= leastsf):
        leastsf = arr[i]

    mpist = arr[i] - leastsf
    if(mpist > dpl[i-1]):
        dpl[i] = mpist
    else:
        dpl[i] = dpl[i-1]

mpibt  = 0
maxat = arr[n-1]
dpr = [0]*n
for i in reversed(range(n-1)):
    if(arr[i]>=maxat):
        maxat = arr[i]
    
    mpibt = maxat - arr[i]
    if(mpibt > dpr[i+1]):
        dpr[i] = mpibt
    else:
        dpr[i] = dpr[i+1] #dpr[i-1]

op = 0
for i in range(n):
    if(dpl[i] + dpr[i] >= op):
        op = dpl[i] + dpr[i]
print(op)