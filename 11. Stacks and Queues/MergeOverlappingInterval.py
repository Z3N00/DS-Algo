


def mergeOverlappingIntervals(arr):

# write your code here
    arr = sorted(arr)
    st = []
    st.append(arr[0])
    idx = 0
 
    for i in range(1, len(arr)):
        if st[idx][1] >= arr[i][0]:
            if st[idx][1] <= arr[i][1]:
                popnum = st.pop()
                st.append([popnum[0], arr[i][1]])    
            else:
                pass

        else:
            st.append(arr[i])
            idx += 1

    for i in range(len(st)):
        print(st[i][0], st[i][1])

    



def main():
    #n = int(input())
    arr = [[22, 28], [1, 8], [25, 27], [14, 19], [27, 30], [5, 12]]


# input from user
    # for i in range(n) :
    #     narr = []
    #     inp = str(input()).strip().split(" ")
    #     narr.append(int(inp[0]))
    #     narr.append(int(inp[1]))
    #     arr.append(narr)


    mergeOverlappingIntervals(arr)



main()