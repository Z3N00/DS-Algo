def main():
    inp = str(input())
    

    # write your code here
    num = 1
    st = []
    for i in range(len(inp)):
        ch = inp[i]
        if ch == 'd':
            st.append(num)
            num += 1
        else:
            st.append(num)
            num += 1

            while len(st) > 0:
                print(st.pop(), end='')
    
    st.append(num)
    while len(st) > 0:
        print(st.pop(), end='')    
    
main()