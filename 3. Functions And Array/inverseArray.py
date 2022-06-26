a = [4, 0, 2, 3, 1]
n = len(a)
inv = n*[None]

for i in range(n):
    val = a[i]
    inv[val] = i

print(inv)