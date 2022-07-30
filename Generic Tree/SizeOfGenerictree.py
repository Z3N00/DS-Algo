class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def constructor(lst, n):
    root = None
    stack = []
    for i in range(len(lst)):
        if i == -1:
            stack.pop()
        else:
            t = Node(lst[i])
            if len(stack) > 0:
                stack[-1].children.append(lst[i])
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

lst = []
n = int(input())
lst = list(map(int, input().split()))
root = constructor(lst,n)
# display(root)
print(size(root))