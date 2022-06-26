



s = "abcc"

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        ss = s[i:j]
        if(ss == ss[::-1]):
            print(ss)

