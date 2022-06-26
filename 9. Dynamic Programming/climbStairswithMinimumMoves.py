from audioop import reverse


def fun(n, jumps, dp):
# write code here
    for i in reverse(range(0, n+1)):
        if(i==n):
            dp[i] == 0
            continue
        minValue = 30
        maxJumps = jumps[i]
        
        j = 1
        while(j<=maxJumps and i+j <= n):
            f = dp[i+j] + 1
            minValue = min(f, minValue)
            j += 1
            dp[i] = minValue

    return dp[0]





# driver code
def main():
    n = int(input())

    jumps = []

    for i in range(n) :
        jumps.append(int(input()))

    dp = [0] * (n + 1)

    ans = fun( n, jumps, dp)

    if (ans < 30):
        print(ans)
    else:
        print("null")

if __name__ == "__main__":
    main()