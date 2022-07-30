import math
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
    
def traversal(root):
   #write your code here
   # area 1 on the way in the recursion, node's pre area
    print(f"Node Pre {root.data}")  # euler left
    for child in root.child:
        # edge pre
        print(f"Edge Pre {root.data} -- {child.data}")
        traversal(child)
        # edge post
        print(f"Edge Post {root.data} -- {child.data}")
    
   # area 2 on the way ou of recursion, node's post area
    print(f"Node Post {root.data}") # euler right
        
lst = []
n = int(input())
lst = list(map(int, input().split()))
root = constructor(lst,n)  
traversal(root)


"""
Node Pre 10
Edge Pre 10--20
Node Pre 20
Node Post 20
Edge Post 10--20
Edge Pre 10--30
Node Pre 30
Edge Pre 30--50
Node Pre 50
Node Post 50
Edge Post 30--50
Edge Pre 30--60
Node Pre 60
Node Post 60
Edge Post 30--60
Node Post 30
Edge Post 10--30
Edge Pre 10--40
Node Pre 40
Node Post 40
Edge Post 10--40
Node Post 10

"""