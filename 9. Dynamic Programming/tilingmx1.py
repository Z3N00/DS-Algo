def No_of_ways(n , m):
    #Write your code here  
    dp = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if(i<m):
            dp[i] = 1
        elif(i==m):
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-m]


    return dp[n]


if __name__ == '__main__':
    
    n = int(input()) #39
    m = int(input()) #16
    
    print(No_of_ways(n , m))   