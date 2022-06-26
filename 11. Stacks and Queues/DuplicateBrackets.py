# 1. You are given a string exp representing an expression. 
# 2. Assume that the expression is balanced i.e. the opening and closing brackets match with each other. 
# 3. But, some of the pair of brackets maybe extra/needless. 
# 4. You are required to print true if you detect extra brackets and false otherwise. 
# e.g.' ((a + b) + (c + d)) -> false (a + b) + ((c + d)) -> true
from collections import deque
st = "(a + b) + ((c + d))"
stack = []

for i in st:
    if(i == ')'):
        if(stack[-1] == '('):
            print("true")
            break
        else:
            while(stack[-1] != '('):
                stack.pop()
            stack.pop()
    else:
        stack.append(i)

print("false")