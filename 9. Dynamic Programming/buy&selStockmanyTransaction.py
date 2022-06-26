def InfiniteTransaction(arr,n):
    # write your code here
    bd = 0
    sd = 0
    profit = 0
    for i in range(n):
        if(arr[i]>=arr[i-1]):
            sd += 1
        else:
            profit += arr[sd] - arr[bd] 
            sd = bd = i
        
    profit += arr[sd] - arr[bd] 
    print(profit)


def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))
        
    InfiniteTransaction(array,n)

if __name__ == '__main__':
    main()
