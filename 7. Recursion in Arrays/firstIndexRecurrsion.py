def find(ar, idx, x):
    if(idx==len(ar)):
        return -1
    
    if(ar[idx] == x):
        return idx
    else:
        num = find(ar, idx + 1, x)
        return num


ar = []
i= 0
n = int(input())
for j in range(n):
    ar.append(int(input()))

print(find(ar, i, 20))
