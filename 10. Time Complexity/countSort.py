import math

def countsort(arr, max, min):
    #write your code here
    range = max - min + 1
    farr = [0] * range
    ans = [0] * len(arr)
    for i in range(len(arr)):
        farr[arr[i] - min] += 1
    
    for i in range(1, len(farr)):
        farr[i] = farr[i-1] + farr[i]

    for i in reversed(range(-1, len(arr)-1)):
        val = arr[i]
        pos = farr[val - min]
        idx = pos - 1
        ans[idx] = val
        farr[val-min] -= 1

    for i in range(len(arr)):
        arr[i] = ans[i] 
    
    

def Display(arr):
    for i in range(0, len(arr)):
        print(arr[i]);


def main():
    n = int(input());
    arr = []
    for i in range(0, n):
        ele = int(input());
        arr.append(ele);

    maxVal = -math.inf;
    minVal = math.inf;
    
    for i in range(0, n):
        minVal = min(minVal, arr[i]);
        maxVal = max(maxVal, arr[i]);

    countsort(arr, maxVal, minVal);
    Display(arr);


if __name__ == "__main__":
    main()