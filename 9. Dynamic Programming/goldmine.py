def fun(n, m, mine):
    dp = mine

    # write code here
    for c in reversed(range(0, m-1)):
        for r in range(0, n):
            if(r == 0):
                dp[r][c] = max(dp[r][c+1], dp[r+1][c+1]) + mine[r][c]
            elif(r==n-1):
                dp[r][c] = max(dp[r-1][c+1], dp[r][c+1]) + mine[r][c]
            else:
                dp[r][c] = max(dp[r-1][c+1], dp[r][c+1], dp[r+1][c+1]) + mine[r][c]

# Here's your Exchange Order number CA-193-8136-0236-EX
    max_gold = 0
    for i in range(n):
        if(dp[i][0] >= max_gold):
            max_gold = dp[i][0]



    return max_gold





# driver code

def main():
  #  n = int(input())
  #  m = int(input())

    mine = [[0,1,4,2,8,2],
            [4,3,6,5,0,4],
            [1,2,4,1,4,6],
            [2,0,7,3,2,2],
            [3,1,5,9,2,4],
            [2,7,0,8,5,1]]

    # for i in range(0, n) :
    #     a = []
    #     l = input()
    #     for j in range(0, m) :
    #         lst = l.split(" ")
    #         val = int(lst[j])
    #         a.append(val)
    #     mine.append(a)


    print(fun(6, 6, mine))

if __name__ == "__main__":
    main()