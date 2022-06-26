n = 3 #int(input())

arr = [10, 20, 30] #[int(input()) for i in range(n)]

k =  1 #int(input())

dp = [[0 for i in range(n)] for j in range(k+1)]
print(dp)
for t in range(1, k+1):
    max = float("-inf")
    for d in range(1, len(arr)):
        if(dp[t-1][d-1] - arr[d-1] > max):
            max = dp[t-1][d-1] - arr[d-1]
        if(max + arr[d] > dp[t][d-1]):
            dp[t][d] = max + arr[d]
            
        else:
            dp[t][d] = dp[t][d-1]
            
        

print(dp[k][n-1])