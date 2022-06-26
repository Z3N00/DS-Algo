s = "PAYPAL"
n = 3

m = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

minRow = 0
minCol = 0

while True:
    for row, col in zip(range(n), range(n)):
        if(row < n):
            m[row][col] = s[i]

    

print(m)