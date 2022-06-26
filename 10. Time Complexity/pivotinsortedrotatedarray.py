def findpivot(arr):
    #write your code here
    low = 0
    hi = len(arr) - 1
    while(low < hi):
        mid = (low+hi)/2
        if(arr[mid] < arr[hi]):
            hi = mid
        else:
            low = mid + 1
    return arr[hi]
    
n=int(input())
arr=[]
for i in range(0,n):
    val=int(input())
    arr.append(val)
pivot=findpivot(arr)
print(pivot)