def mergeArrays(arr1, arr2, n1, n2):
	# write your code
    i = 0
    j = 0
    ans = []
    k = 0
    while k < (n1+n2):
        
        if(i == n1 and j<n2):
            ans.append(arr2[j])
            j += 1
        elif(j == n2 and i<n1):
            ans.append(arr1[i])
            i += 1
        elif((i<=n1) and (j<=n2)):
            if(arr1[i] >= arr2[j]):
                ans.append(arr2[j])
                j += 1
            elif(arr2[j] >= arr1[i]):
                ans.append(arr1[i])
                i += 1
        
        k += 1
    for i in ans:
        print(i)

# arr1= []

# n = int(input())

# for i in range(0, n):
# 	ele = int(input())
	
# 	arr1.append(ele)
	
# arr2 =[]
# m = int(input())

# for i in range(0, m):
# 	ele = int(input())

# 	arr2.append(ele) 
	
mergeArrays([-1, 0], [0, 1], 2, 2)