def paintHousemantcolors():
    n, k  = map(int, input().split())
    arr = []
    for i in range(n):
        arr.insert(i, list(map(int, input().split())))

    least  = 99999999
    sleast = 99999999

    dp = [[0 for i in range(k)] for j in range(n)]

    for col in range(k):
        dp[0][col] = arr[0][col]

        if(arr[0][col] <= least):
            sleast = least
            least = arr[0][col]
        elif(arr[0][col]<= sleast):
            sleast = arr[0][col]
        
    for i in range(len(dp)):
        nleast = float('inf')
        nsleast = float('inf')
        for j in range(len(dp[0])):
            if(least == dp[i-1][j]):
                dp[i][j] = sleast + arr[i][j]
            else:
                dp[i][j] = least + arr[i][j]

            
            if(dp[i][j] <= nleast):
                nsleast = nleast
                nleast = dp[i][j]
            elif(dp[i][j]<= nsleast):
                nsleast = dp[i][j]


        least = nleast
        sleast = nsleast
        
    

    print(least)


paintHousemantcolors()