def encoding():
    str = input()

    dp = [0]*len(str)

    dp[0] = 1

    for i in range(1, len(dp)):
        if(str[i-1]=='0' and str[i]=='0'):
            dp[i] = 0
        elif(str[i-1] == '0' and str[i]!='0'):
            dp[i] = dp[i-1]

        elif(str[i-1]!='0' and str[i]=='0'):
            if(str[i-1]=='1' or str[i-1]=='2'):
                dp[i] = (dp[i-2]if(i>=2) else 1)
            else:
                dp[i] = 0
        else:
            if(int(str[i-1: i+1])<=26):
                dp[i] = dp[i-1] + (dp[i-2] if i>=2 else 1)
            else:
                dp[i] = dp[i-1]


    print(dp[len(str)-1])


encoding()