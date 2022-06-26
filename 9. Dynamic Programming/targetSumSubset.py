def targetsum(n, arr, tar, dp):
    #  write your code here
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if(i==0 and j==0):
                dp[i][j] = True
            elif(i==0):
                dp[i][j] = False
            elif(j==0):
                dp[i][j] = True
            else:
                if(dp[i-1][j] == True):
                    dp[i][j] = True
                else:
                    val = arr[i-1]
                    if(j >= val):
                        if(dp[i-1][j-val]==True):
                            dp[i][j] = True
    return dp[len(arr)][tar]



n = int(input())
arr = []
for i in range(n) :
    x = int(input())
    arr.append(x)
tar = int(input())

dp = [[False for x in range(tar + 1)] for y in range(n + 1)]
print(targetsum(n, arr, tar, dp))

