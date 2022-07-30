class Node:
     
    def __init__(self, key):
         
        self.key = key
        self.child = []

def newNode(key):   
    temp = Node(key)
    return temp

def constructor(lst,n):
    root = None
    stack = []
    for i in range(0,n):
        if lst[i]==-1:
            stack.pop()
        else:
            t= Node(lst[i])
            if len(stack) > 0:
                stack[-1].child.append(t)
                
            else:
                root=t
                
            stack.append(t)
    return root
    
def LevelOrderTraversal(root):
  #write your code here

  q = []
  q.append(root)
  while len(q) > 0:
    root = q.pop(0)
    print(str(root.key) + "", end = " ")
    for child in root.child:
        q.append(child)

  print(".")

        
lst = []
n = int(input())
lst = list(map(int, input().split()))
root = constructor(lst,n)  
LevelOrderTraversal(root)