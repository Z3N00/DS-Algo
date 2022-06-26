n = 57
b = 2
i = 0
res = 0
while(n!=0):
    num = n%b
    res = res + num * (10**i)
    i+=1
    n = int(n/2)
print(res)