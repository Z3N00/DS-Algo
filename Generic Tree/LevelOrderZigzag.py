


class Node:
     
    def _init_(self, key, child):
         
        self.key = key
        self.child = []
   
 # Utility function to create a new tree node
def newNode(key):   
    temp = Node()
    temp.key = key;
    temp.child = []
    return temp
    

# Prints the n-ary tree level wise
def constructor(lst,n):
    root = None
    stack = []
    for i in range(0,n):
        if lst[i]==-1:
            stack.pop()
        else:
            t= newNode(lst[i])
            if len(stack) > 0:
                stack[-1].child.append(t)
                
            else:
                root=t
                
            stack.append(t)
    return root
    
def Linewisezigzag(root):
  
  # write code heres
    ms = []
    cs = []
    level = 1
    ms.append(root)
    while len(ms) > 0 :
        root = ms.pop()
        print(root.key, end=" ")
        if level % 2 == 1:
            for i in range(len(root.child)):
                child = root.child[i]
                cs.append(child)
        else:
            for i in range(len(root.child)-1,-1,-1):
                child = root.child[i]
                cs.append(child)
        if len(ms) == 0:
            ms = cs
            cs = []
            level += 1
            print()
lst = []
# number of elements as input
n = int(input())
# s1 =input().split()
# values = input().split()

lst = list(map(int, input().split()))
     
# print(lst)
root = constructor(lst,n) 
# print(root.child[0].child[0].key)
Linewisezigzag(root)
