# 1. You are given a string exp representing an expression.
# 2. You are required to check if the expression is balanced i.e. closing brackets and opening brackets match up well.

# e.g.
# [(a + b) + {(c + d) * (e / f)}] -> true
# [(a + b) + {(c + d) * (e / f)]} -> false
# [(a + b) + {(c + d) * (e / f)} -> false
# ([(a + b) + {(c + d) * (e / f)}] -> false

from cmath import exp

from numpy import False_


def balanced_brackets(expression):
    stack  = []
    for char in expression:
        if(char == '[' or char == '{' or char == '('):
            stack.append(char)
        elif(char == ']'):
            if(len(stack)==0):
                return False
            elif(stack[-1] != '['):
                return False
            else:
                stack.pop()
                return True
        elif(char == '}'):
            if(len(stack)==0):
                return False
            elif(stack[-1] != '{'):
                return False
            else:
                stack.pop()
                return True
        elif(char == ')'):
            if(len(stack)==0):
                return False
            elif(stack[-1] != '('):
                return False
            else:
                stack.pop()
                return True

    if(len(stack) == 0):
        return True
    else:
        return False