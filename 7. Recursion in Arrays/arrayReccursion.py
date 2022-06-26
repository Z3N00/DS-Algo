def da(ar, i):
    if(i == len(ar)-1):
        return ar[i]
    mis = da(ar, i+1)
    
    if(mis > ar[i]):
        return mis
    else:
        return ar[i]



ar = []
i= 0
n = int(input())
for j in range(n):
    ar.append(int(input()))

max = da(ar, i)
print(max)