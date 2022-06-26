def oneTransaction(arr,n):
    # write your code here
    dp = [[0 for i in range(n+1)] for j in range(len(arr))]
    max_profit = dp[0][0]

    for i in range(len(arr)):
        for j in range(i+2, n+1):
            if(j == 0 or j == 1):
                dp[i][j] = 0
            elif(i==len(arr)-1):
                dp[i][j] = 0
            else:
                dp[i][j] = arr[j-1] - arr[i]
               # max_profit = dp[i][j] if dp[i][j] >= max_profit else max_profit
                if(dp[i][j]>= max_profit):
                   max_profit = dp[i][j]
    print(dp)
    print("Profit:", max_profit)


def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))
        
    oneTransaction(array,n)

if __name__ == '__main__':
    main()