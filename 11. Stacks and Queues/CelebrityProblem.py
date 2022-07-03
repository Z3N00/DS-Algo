def findCelebrity(arr):
# write your code here
    st = []
    for i in range(len(arr)):
        st.append(i)

    while len(st) > 1:
        i = st.pop()
        j = st.pop()

        if(arr[i][j] == 1):
            # If i knows j then i is not a celebrity
            st.append(j)
        else:
            # If i does not know j then j is not a celebrity
            st.append(i)

    pot = st.pop()
    flag = True
    for i in range(len(arr)):
        if(i != pot):
            if(arr[i][pot] == 0 or arr[pot][i] == 1):
                flag = False
                break
    if flag:
        print(pot)
    else:
        print("none")

#n = int(input())
# arr = [[int(input()) for j in range(n)] for i in range(n)]

#n = int(input())
arr = [[0,0,0,0], [1,0,1,1], [1,1,0,1], [1,1,1,0]]

# for i in range(n) :
#     row = input()
#     arr.append(row)
findCelebrity(arr)