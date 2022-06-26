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

def selectionSort(arr):
    # write your code
    for itr in range(len(arr)-1):
        min = itr
        for j in range(itr+1, len(arr)):
            if(isSmaller(arr, j, min)):
                min = j
        swap(arr, itr, min)



def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end="\n")
	print()



arr = []

n = 5 #int(input())
arr = [7, -2, 4, 1, 3]
# for i in range(0, n):
# 	ele = int(input())

# 	arr.append(ele) # adding the element
selectionSort(arr)
printList(arr)