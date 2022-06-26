# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))
  
# # Initialize matrix
# matrix = []
# print("Enter the entries rowwise:")
  
# # For user input
# for i in range(R):          # A for loop for row entries
#     a =[]
#     for j in range(C):      # A for loop for column entries
#          a.append(int(input()))
#     matrix.append(a)
  
# # For printing the matrix
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end = " ")
#     print()




# for i in range(4):
#     for j in range(4):
#         print(m[i][j], end=" ")
#     print()


def main():
    row = int(input())
    col = int(input())
    m = []

    for i in range(row):          
        a =[]
        for j in range(col):      
            a.append(int(input()))
        m.append(a)
   # m = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    s = 2
    r = 1
    oneD = oneDarray(m, s)
    singleMatrix = rotate(oneD, r)
    fillOneDarray(m, singleMatrix, s)
    display(m, 4, 4)

def display(m, row, col):
    for i in range(row):
        for j in range(col):
            print(m[i][j], end=" ")
        print()


def oneDarray(m, s):
    rmin = s-1
    cmin = s-1
    rmax = len(m) - s
    cmax = len(m[0]) - s

    sz = 2*((rmax - rmin) + (cmax - cmin))

    oneD = [None]*sz

    #lw
    idx = 0
    for i in range(rmin, rmax+1):
        j = cmin
        oneD[idx] = m[i][j]
        idx += 1
    #bw
    for j in range(cmin, cmax+1):
        i = rmax
        oneD[idx] = m[i][j]
        idx +=1
    #rw
    for i in range(rmax-1, rmin-1, -1):
        j = cmax
        oneD[idx] = m[i][j]
        idx +=1
    #tw
    for j in range(cmax-1, cmin, -1):
        i = rmin
        oneD[idx] = m[i][j]
        idx +=1

    return oneD  

def rotate(oneD, r):
    if(r<0):
        r += len(oneD) 

    r = r % len(oneD)
    ar1 = []
    ar2 = []
    for i in range(len(oneD)-r):
        ar1[i] = oneD[i]
    
    idx=0
    for i in range(len(oneD)-r+1, len(oneD)):
        ar2[idx] = oneD[i]    
        idx+=1
    
    new_list = ar1[::-1] + ar2[::-1]
    oneD = new_list[::-1]

    return oneD

def fillOneDarray(m, oneD, s):
    rmin = s-1
    cmin = s-1
    rmax = len(m) - s
    cmax = len(m[0]) - s


    #lw
    idx = 0
    for i in range(rmin, rmax+1):
        j = cmin
        m[i][j]= oneD[idx]
        idx += 1
    #bw
    for j in range(cmin, cmax+1):
        i = rmax
        m[i][j]= oneD[idx]
        idx +=1
    #rw
    for i in range(rmax, rmin-1, -1):
        j = cmax
        m[i][j]= oneD[idx]
        idx +=1
    #tw
    for j in range(cmax, cmin-1, -1):
        i = rmin
        m[i][j]= oneD[idx]
        idx +=1

    return m 

main()