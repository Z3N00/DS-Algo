a = [10, 20, 30]
n = len(a)
for i in range(n):
    k = n 
    for j in range(i, n-k-i):
        print(a[j], end="")
    print()