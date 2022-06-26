n1 = 2
m1 = 3

a1 = []

for i in range(n1):
    a = []
    for j in range(m1):
        a.append(int(input()))
    a1.append(a)

n2 = 3
m2 = 4

a2 = []

for i in range(n2):
    a = []
    for j in range(m2):
        a.append(int(input()))
    a2.append(a)

a3 = []

if(m1!=n2):
    print("Invalid input")


for i in range(n1):
    sum = 0
    for j in range(m2):
        for k in range(m1):
            sum = sum + a1[i][k]*a2[k][j]
        a3[i][j].append(sum)


for i in range(n1):
    for j in range(m2):
        print(a3[i][j], end=" ")
    print()