def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def merge(fsh, ssh):
    n1=len(fsh)
    n2=len(ssh)
    
    L=[0]*(n1)
    R=[0]*(n2)
    
    print("Merging these two arrays ")
    print("left array -> ",end="")
    
    for i in range(0,n1):
        L[i]=fsh[i]
        
    printList(L)
    
    print("right array -> ",end="")
    for j in range(0,n2):
        R[j]=ssh[j]
        
    printList(R)
    i=0
    j=0
    k=0
    
    while i<n1 and j<n2:
        if L[i] <=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
        
        
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
        
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
    
def mergeSort(arr,l,r):
  # write your code
    if(l == r):
        ba = [0]
        ba[0] = arr[l]
        return ba
    
    mid = (l+r)/2
    fsh = mergeSort(arr, l, mid)
    ssh = mergeSort(arr, mid+1, r)
    fsa = merge(fsh, ssh)
    return fsa        
    
arr=[]

n=int(input())

for i in range(0,n):
    ele=int(input())
    
    arr.append(ele)
    

mergeSort(arr,0,n-1)
print("Sorted Array -> ",end="")
printList(arr)