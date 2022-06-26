n = 4

m =  [[j for j in input().strip()] for i in range(n)] 

sNo = m[0][0]
col = 0

for i in range(n):
    for j in range(n):
        if(m[i][j]<=sNo):
            sNo = m[i][j]
            col = j

lNo = m[0][col]
for i in range(n):
    if(m[i][col]>=lNo):
        lNo = m[i][col]

print(lNo)