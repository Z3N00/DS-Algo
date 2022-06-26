def printlist(arr):
    for i in arr:
        print(i)

# used for swapping ith and jth elements of array
def swap(arr, i, j):
    print("Swapping index" , i , "and index" ,j);
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;

def sort012(arr):
    #write your code here
    i,j = 0,0
    k = len(arr) - 1

    while(i <= k):
        if arr[i] == 1:
            i += 1
        elif arr[i] == 0:
            swap(arr, i, j)
            i += 1
            j += 1
        elif arr[i] == 2:
            swap(arr, i, k)
            k -= 1



#n = int(input());
A= [1,0,2,2,1,0,2,1,0,2];
# for i in range(0, n):
#     val = int(input());
#     A.append(val) ;
sort012(A);
printlist(A);