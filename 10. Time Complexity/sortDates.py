def Display(arr):
    for i in arr:
        print(i)
    

def countsort(arr, d, mod, r):
    # write your code here
    farr = [0] * r
    ans = [0] * len(arr)
    for i in range(len(arr)):
        idx = (int(arr[i], 10)//d)%mod  
        farr[idx] += 1
    
    for i in range(1, len(farr)):
        farr[i] = farr[i-1] + farr[i]

    for i in reversed(range(-1, len(arr)-1)):
        idx = (int(arr[i], 10)//d)%mod
        ans[farr[idx]-1] = arr[i]
        farr[idx] -= 1

    for i in range(len(arr)):
        arr[i] = ans[i] 
    

def sortDates(arr):
    # write your code here
    countsort(arr, 1000000, 100, 32) # days
    countsort(arr, 10000, 100, 13) # months
    countsort(arr, 1, 10000, 2501) #years


def main():
    n = int(input())
    arr = []
    for i in range(0, n):
        ele = (input())
        arr.append(ele)
    
    sortDates(arr)
    Display(arr)
    
    
if __name__ == "__main__":
    main()
    