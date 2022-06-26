n = 4
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# for i in range(n):
#     a = []
#     for j in range(n):
#         a[i][j] = int(input())
#     m.append(a)

for g in range(n):
    for i,j in zip(range(n), range(g, n)):
        print(m[i][j])