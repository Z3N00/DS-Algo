def abcSequence(st):
    a = 0
    ab = 0
    abc = 0

    for i in range(len(st)):
        ch = st[i]

        if(ch == 'a'):
            a = 2*a + 1
        elif(ch == 'b'):
            ab = 2*ab + a
        elif(ch == 'c'):
            abc = 2*abc + ab

    print(abc)


abcSequence('abcabc')