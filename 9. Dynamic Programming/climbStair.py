
    # Memorisation method dynamic programming
def stairCaseMemorisation(n, qb):
    if(n == 0):
        return 1
    elif(n<0):
        return 0

    if(qb[n]>0):
        return qb[n]

    x = stairCaseMemorisation(n-1, qb)
    y = stairCaseMemorisation(n-2, qb)
    z = stairCaseMemorisation(n-3, qb)

    total = x+y
    qb[n] = total
    return total


    # Tabulation method dynamic programming

def stairCaseTabulation(n):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if(i == 1):
            dp[i] = dp[i-1]
        elif(i == 2):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


#print(stairCaseMemorisation(4, [0]*5))

print(stairCaseTabulation(5))