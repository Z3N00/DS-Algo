def slidingWindow(arr, k1):
    # write your code here
    st = []
    index = 0
    while index <= len(arr):
        if(len(arr) - index <= k1):
            st.append(max(arr[index:len(arr)+1]))
        else:
            st.append(max(arr[i:k1+i+1]))

    print(st)


n = int(input())
arr = [] * n
for i in range(n) :
    x = int(input())
    arr.append(x)
k = int(input())

slidingWindow(arr, k)