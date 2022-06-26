import math;

def Display(arr):
    for i in arr:
        print(i,end = " ")

def countsort(arr, d):
    # write your code here
    
    farr = [0] * 10
    ans = [0] * len(arr)
    for i in range(len(arr)):
        farr[arr[i]/d%10] += 1
    
    for i in range(1, len(farr)):
        farr[i] = farr[i-1] + farr[i]

    for i in reversed(range(-1, len(arr)-1)):
        val = arr[i]
        pos = farr[val/d%10]
        idx = pos - 1
        ans[idx] = val
        farr[val/d%10] -= 1

    for i in range(len(arr)):
        arr[i] = ans[i] 
    
    
    print("After sorting on" , d , "place ->", end = " ");
    Display(arr);
    print();


def radixSort(arr):
    # write your code here
    max = float("-inf")
    for val in arr:
        if max > val:
            max = val
    
    exp = 1
    while(exp<=max):
        countsort(arr, exp)
        exp = exp*10



def main():
    n = int(input());
    arr = []
    for i in range(0, n):
        ele = int(input());
        arr.append(ele);

    
    radixSort(arr);
    Display(arr);
    

if __name__ == "__main__":
    main()