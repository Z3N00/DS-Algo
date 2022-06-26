def perm(s, ans):
    if(len(s) == 0):
        print(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        leftsubstring = s[0:i]
        rightSunstring = s[i+1:]
        ros = leftsubstring + rightSunstring
        perm(ros, ans + ch)



perm("abcd", "")