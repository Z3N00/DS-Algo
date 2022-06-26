def zeroknapSack(cap, wt, val, n):

    dp = [[0 for i in range(cap + 1)] for j in range(n+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if(j>=wt[i-1]):
                remCap = j - wt[i-1]
                if(dp[i-1][remCap] + val[i-1] > dp[i-1][j]):
                    dp[i][j] = dp[i-1][remCap] + val[i-1]
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][cap]


n = int(input())

st1 = input()
v = st1.split()
val = [int(i) for i in v]

st2 = input()
w = st2.split()
wt = [int(j) for j in w]

cap = int(input())

print(zeroknapSack(cap, wt, val, n))