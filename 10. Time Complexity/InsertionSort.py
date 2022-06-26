def swap(arr,i,j):
    print("Swapping",arr[i],"and",arr[j])
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def isGreater(arr,j,i):
    print("Comparing",arr[i],"and",arr[j])

    if arr[i]<arr[j]:
        return True
    else :
        return False

def insertionSort(arr):
    #write your code
    for i in range(1, len(arr)):
        for j in range(i-1,-1, -1):
            if(isGreater(arr, j, j+1)):
                swap(arr, j, j+1)
            else:
                break

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end="\n")
	print()



arr = []

n = int(input())

for i in range(0, n):
	ele = int(input())

	arr.append(ele) # adding the element
insertionSort(arr)
printList(arr)