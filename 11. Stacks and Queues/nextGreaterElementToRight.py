from sys import stdin
def display(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = "\n")
def solve(arr2):
    #write your code here
    a = [0] * len(arr2)
    stack = []
    a[-1] = -1
    stack.append(arr2[len(arr2) - 1])
    for i in reversed(range(len(arr2)-2)):
        while len(stack) > 0 and stack[-1] <= arr2[i]:
            stack.pop()
        if(len(stack) == 0):
            a[i] = -1
        else:
            a[i] = stack[-1]

        stack.append(arr2[i])
    
    return a
 
        

n = 9
arr = [2, 5, 9, 3, 1, 12, 6, 8, 7]
# for i in range (n):
#     x = int(input())
#     arr.append(x)

nge = solve(arr)
display(nge)