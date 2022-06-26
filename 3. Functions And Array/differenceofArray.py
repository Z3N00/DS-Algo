a1 = [1]
a2 = [1,0,0]
n = len(a2) 
diff = n*[None]

c  = 0
i = len(a1) - 1
j = len(a2) - 1
k = len(a2) - 1
while(k>=0):
    d = 0
    a1v = a1[i] if i>=0 else 0

    if(a2[j]+c >= a1v):
        d = a2[j]+c - a1v
    else:
        d = a2[j] + c + 10 - a1v
        c = -1

    diff[k] = d
    i-=1
    j-=1
    k-=1

idx = 0
while(idx<len(diff)):
    if(diff[idx]==0):
        idx+=1
    else:
        break
while(idx<len(diff)):
    print(diff[idx])
    idx+=1

