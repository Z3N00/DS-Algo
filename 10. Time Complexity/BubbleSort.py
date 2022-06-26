def swap(arr,i,j):
    print("Swapping",arr[i],"and",arr[j])
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def isSmaller(arr,i,j):
    print("Comparing",arr[i],"and",arr[j])

    if arr[i]<arr[j]:
        return True
    else :
        return False

def bubbleSort(arr):
  # write your code
    for itr in range(1, len(arr)):
        
        for j in range(len(arr)-itr):
            if(isSmaller(arr, j+1, j)):
                swap(arr, j+1, j)
                
    printList(arr)

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end="\n")
	print()


n = 5
arr = [7, -2, 4,  1, 3]
bubbleSort(arr)


"""
Comparing -2 and 7
Swapping -2 and 7
Comparing 4 and 7
Swapping 4 and 7
Comparing 1 and 7
Swapping 1 and 7
Comparing 3 and 7
Swapping 3 and 7
Comparing 4 and -2
Comparing 1 and 4
Swapping 1 and 4
Comparing 3 and 4
Swapping 3 and 4
Comparing 1 and -2
Comparing 3 and 1
Comparing 1 and -2

"""