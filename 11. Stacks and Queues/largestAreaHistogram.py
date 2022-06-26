from sys import stdin
n = int(input())
arr = []
for i in range (n) :
  x = int(input())
  arr.append(x)

#write your code here

rb = [0]*len(arr) # next smaller index on the right
st = []
st.append(len(arr) - 1)
rb[len(arr) - 1] = len(arr)

for i in range(len(arr)-2, -1, -1):
    while len(st) > 0 and arr[i] < arr[st[-1]]:
        st.pop()
        
    if len(st) == 0:
        rb[i] = len(arr)
    else:
        rb[i] = st[-1]
    st.append(i)


lb = [0]*len(arr) # next smaller index on the left
st = []
st.append(0)
lb[0] = -1

for i in range(1, len(arr)):
    while len(st) > 0 and arr[i] < arr[st[-1]]:
        st.pop()
        
    if len(st) == 0:
        lb[i] = -1
    else:
        lb[i] = st[-1]
    st.append(i)

maxArea = 0
for i in range(len(arr)):
    width = rb[i] - lb[i] - 1
    area = arr[i] - width
    if area > maxArea:
        maxArea = area
        
        
        
print(maxArea)