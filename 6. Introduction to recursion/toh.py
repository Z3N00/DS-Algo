def toh(n, s, d, h):
    if n == 0:
        return
    toh(n-1, s, h, d)
    print(n , "[" , s,  " -> " , d, "]")
    toh(n-1, h, d, s)


n = int(input())
s = int(input())
d = int(input())
h = int(input())
toh(n, s, d, h)