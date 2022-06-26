arr = [1,2,3,4,5]
span = []

st = []

st.append(0)
span.append(1)

for i in range(1, len(arr)):
    while(len(st) > 0 and arr[i]>arr[st[-1]]):
        st.pop()
    if len(st) == 0:
        span.append(i+1)
    else:
        span.append(i - st[-1])

    st.append(i)
    
print(span)  