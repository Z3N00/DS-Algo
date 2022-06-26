n = 10
b = 2
ans = 0
i = 0
while(n!=0):
    num = n%2
    ans = ans + num*(10**i)
    i+=1
    n=int(n/2)

print(int(ans))