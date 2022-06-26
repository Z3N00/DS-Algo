def swap(arr,i,j):
    print("Swapping",arr[i],"and",arr[j])
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp


def partition(arr,pivot):
    # 0 to j-1 -> <= pivot
    # j to j-1 -> > pivot
    # i to end -> unknown

    i = 0
    j = 0
    while(i<len(arr)):
        if(arr[i]>pivot):
            i += 1
        else:
            swap(arr, i, j)
            i += 1
            j += 1





def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()



arr = []

n = int(input())

for i in range(0, n):
	ele = int(input())

	arr.append(ele) 


pivot = int(input())

partition(arr,pivot)
printList(arr)