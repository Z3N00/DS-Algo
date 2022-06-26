from pandas import pivot


def swap(arr, i, j):
    print("Swapping", arr[i] , "and" , arr[j]);
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    

def partition(arr, pivot, lo, hi):
    print("pivot ->" , pivot);
    curr = lo;
    prev = lo - 1;
    while(curr <= hi):
        if(arr[curr] <= pivot):
            prev = prev + 1;
            swap(arr, curr, prev);
        curr = curr + 1;
        
    print("pivot index ->" , prev);
    return prev;
    
def quicksort(arr, lo, hi):
    # write your code here
    if(lo>hi):
        return
    pivot = arr[hi]
    pi = partition(arr, pivot, lo, hi)
    quicksort(arr, lo, pi-1)
    quicksort(arr, pi+1, hi)
    
def Display(arr):
    for i in range(0, len(arr)):
        print(arr[i] ,end = " ");

def main():
    n = int(input());
    arr = []
    for i in range(0, n):
        ele = int(input());
        arr.append(ele);

    quicksort(arr, 0, n-1);
    Display(arr);


if __name__ == "__main__":
    main()      