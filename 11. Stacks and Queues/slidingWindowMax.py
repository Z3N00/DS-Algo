def slidingWindow(arr, k1):
    # write your code here
    st = []
    index = 0
    while index < len(arr):
        if(len(arr) - index >= k1):
            st.append(max(arr[index:k1+index]))
            index = index + 1
        else:
            break
           

    for i in st:
        print(i)


# n = int(input())
# arr = [] * n
# for i in range(n) :
#     x = int(input())
#     arr.append(x)
# k = int(input())

slidingWindow([1,2,3,4], 2)

""" pep coding code by sliding window"""


# def slidingWindow(arr, k1):
#   st = []
#        n = len(arr)
#            ngr = [0] * n     # next greater elemment on right
#                  for i in reversed(range(n - 1)) :
#                while len(st) > 0 and arr[i] >= arr[st[-1]]:
#                      st.pop()
#                if len(st) == 0:
#                        ngr[i] = (n)
#                         else:
#                                   ngr[i] = (st[-1])
#                                            st.append(i)



#                                            ans = [0] * (n - k1 + 1)
#                                                  j = 0
#                                                      for i in range(n - k1 + 1) :
#                                            if j < i:
#                                                        j = i
#                                                            ep = i + k1     # window size i + k
#                                                    while ngr[j] < ep:
#                                                                    j = ngr[j]
#                                                                        ans[i] = arr[j]

#                                                            for i in ans :
#                                                                            print(i)

#                                                                              n = int(input())
#                                                                                  arr = [] * n
#                                                                                      for i in range(n) :
#                                                                                        x = int(input())
#                                                                                            arr.append(x)
#                                                                                            k = int(input())

#                                                                                                slidingWindow(arr, k)