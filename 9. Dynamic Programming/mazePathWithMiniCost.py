def fun(n, m, arr):
    dp = [[0 for c in range(m)] for r in range(n)]

# write code here

    for r in reversed(range(0, n)) :
        for c in reversed(range(0, m)) :
            if (r == n - 1 and c == m - 1):
                dp[r][c] = arr[r][c]
            elif(r == n - 1):
                dp[r][c] = dp[r][c + 1] + arr[r][c]
            elif(c == m - 1) :
                dp[r][c] = dp[r + 1][c] + arr[r][c]
            else :
                dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + arr[r][c]

    return dp[0][0]


# driver code

def main():
    n = int(input())
    m = int(input())

    arr = []

    for i in range(0, n) :
        ar = []
        l = input()
        for j in range(0, m) :
            lst = l.split(" ")
            val = int(lst[j])
            ar.append(val)
        arr.append(ar)



    print(fun(n, m, arr))

if __name__ == "__main__":
    main()