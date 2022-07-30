class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

def constructor(lst, n):
    root =  None
    stack = []
    for i in range(n):
        if lst[i] == -1:
            stack.pop()
        else:
            t = Node(lst[i])
            if len(lst) > 0:
                stack[-1].children.append(t)
            else:
                root = t
            stack.append(lst[i])
    return root

def display(root):
    s = str(root.data) + "->"
    for child in root.children:
        s += str(child.data) + ", "
    s += "."
    print(s)
    for child in root.children:
        display(child)

def size(root):
    s = 0
    for child in root.children:
        cs = size(child)
        s = s + cs

    s += 1
    return s


def maximum(root):
    maxNum = float("-inf")
    for child in root.children:
        cm = maximum(child)
        maxNum = max(cm, maxNum)

    maxNum = max(root.data, maxNum)
    return maxNum