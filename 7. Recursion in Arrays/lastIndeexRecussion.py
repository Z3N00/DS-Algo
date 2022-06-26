def find(ar, idx, x):
    if(idx==len(ar)):
        return -1
    num = find(ar, idx + 1, x)
    if num == -1:
        if(ar[idx] == x):
            return idx
        else:
        
            return -1
    else:
        return num


ar = []
i= 0
n = int(input())
for j in range(n):
    ar.append(int(input()))
x = int(input())
print(find(ar, i, x))