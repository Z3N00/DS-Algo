

def encoding(st, ans):
    if(len(st)==0):
        print(ans)
        return
    elif(len(st)==1):
        ch = st[0]
        if(ch=='0'):
            return
        else:
            code = chr(ord('a') + int(ch) - 1)
            ans = ans + code
            print(ans)

    else:
        ch = st[0]
        ros = st[1:]
        if(ch=='0'):
            return
        else:
            code = chr(ord('a') + int(ch) - 1)
            encoding(ros, ans + code)

            
        ch12 = st[0:2]
        ros12 = st[2:]
        if(int(ch12)<=26):
            code = chr(ord('a') + int(ch12) - 1)
            encoding(ros12, ans + code)
    print(count)


count = 0
encoding("655196", "", count)