def fun(n, arr, dp):

# write code here
    
    for i in reversed(range(0, n + 1)) :
        if (i == n):
            dp[i] = 1
            continue
        maxjump = arr[i]

        ans = 0

        j = 1
        while (j <= maxjump and i + j <= n):
            ans = ans + dp[ i + j ]
            j += 1

            dp[i] = ans


    return dp[0]


# driver code
def main():
    n = 6
    arr = [2, 3, 2, 4, 0, 1]

    # for i in range(0, n) :
    #     arr.append(int(input()))

    dp = [0] * (n + 1)

    print(fun(n, arr, dp))

if __name__ == "__main__":
    main() 