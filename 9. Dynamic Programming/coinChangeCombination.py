def CountCombination(n, arr, amt):
    dp = [0] * (amt + 1)
    for i in arr:
        for j in range(i, amt+1):
            dp[0] = 1
            dp[j] += dp[j - i]



    print(dp[amt])





def main():
    n = 4
    arr = [2, 3, 5, 6]
    amt = 7

    CountCombination(n, arr, amt)

main()