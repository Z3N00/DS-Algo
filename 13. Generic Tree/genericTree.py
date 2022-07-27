class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []



def constructor(self, list, n):
    root = None
    stack = []
    for i in range(n):
        if list[i] == -1:
            stack.pop()
        else:
            t = Node(list[i])
            if len(stack) > 0:
                stack[-1].children.append(t)
            else:
                root = t 
            stack.append(t)
    return root



# d(10) -> 10 will print itself and it's family
# d(20), d(30), d(40) will print themselves and their family
# d(10) = s(10) + d(20) + d(30) + d(40)
def display(self, node):
    s = str(node.data) + "->"
    for child in node.children:
        s += str(child.data) + ", "
    s += "."
    print(s)
    for child in node.children:
        self.display(child)





lst = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, -1, 40, 80, -1, -1, -1]
n =  16 #int(input())
#lst = list(map(int, input().split()))
root = Node().constructor(lst,n)
Node().display(root)