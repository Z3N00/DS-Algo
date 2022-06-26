def unbounded_knapSack(cap, wt, val, n):

# write your code here
    dp = [0] * (cap+1)

    for bcap in range(1, cap+1):
        max = 0
        for i in range(n):
            if(wt[i] <= bcap):
                rbagc = bcap- wt[i]
                rbagv = dp[rbagc]
                tbagv = rbagv + val[i]

                if(tbagv > max):
                    max = tbagv

        dp[bcap] = max
    return dp[cap]

n = int(input())

st1 = input()
v=st1.split()
val=[int(i) for i in v]

st2 = input()
w = st2.split()
wt = [int(j) for j in w]

cap = int(input()) 
 
print(unbounded_knapSack(cap, wt, val, n))