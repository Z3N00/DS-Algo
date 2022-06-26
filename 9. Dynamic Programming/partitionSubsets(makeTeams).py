def Partition_into_subsets(n , k):
    # write your code here
    dp = [[0 for i in range(n+1)] for j in range(k+1)]

    if(n==0 or k==0 or n<k):
        print(0)

    for t in range(1, k+1):
        for p in range(1, n+1):
            if(p<t):
                dp[t][p] = 0
            elif(t==p):
                dp[t][p] = 1
            else:
                dp[t][p] = t*(dp[t][p-1]) + dp[t-1][p-1]

    return dp[k][n]
    
if __name__ == '__main__':
    n = int(input())
    k = int(input())
    
    print(Partition_into_subsets(n , k)) 