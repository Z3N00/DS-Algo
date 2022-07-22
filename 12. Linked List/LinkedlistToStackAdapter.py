class Node:

    def __init__(self):
        self.data = 0
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addLast(self, val):
        temp = Node()
        temp.data = val
        temp.next = None

        if self.size == 0:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1
       
    def getNodeAt(self, idx):
        temp = self.head
        i = 0
        while i < idx:
            temp = temp.next
            i += 1
        return temp
       
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
        print()
       
    def removeFirst(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = self.head.next
            self.size -= 1
           
    def getFirst(self):
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            return self.head.data

    def getLast(self):
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            return self.tail.data
           
    def getAt(self, idx):
        if self.size == 0:
            print("List is empty")
            return -1
        elif idx < 0 or idx >= self.size:
            print("Invalid arguments")
            return -1
        else:
            temp = self.head
            i = 0
            while i < idx:
                temp = temp.next
                i += 1
            return temp.data
           
    def addFirst(self, val):
        temp = Node()
        temp.data = val
        temp.next = self.head
        self.head = temp

        if self.size == 0:
            self.tail = temp

        self.size += 1
           
    def removeAt(self, idx):
        if idx < 0 or idx >= self.size:
            print("Invalid arguments")
        elif idx == 0:
            self.removeFirst()
        elif idx == self.size - 1:
            self.removeLast()
        else:
            temp = self.head
            i = 0
            while i < idx - 1:
                temp = temp.next
                i += 1

            temp.next = temp.next.next
            self.size -= 1

    def addAt(self, idx, val):
        if idx < 0 or idx > self.size:
            print("Invalid arguments")
        elif idx == 0:
            self.addFirst(val)
        elif idx == self.size:
            self.addLast(val)
        else:
            node = Node()
            node.data = val

            temp = self.head
            i = 0
            while i < idx - 1:
                temp = temp.next
                i += 1
            node.next = temp.next

            temp.next = node
            self.size += 1
           
    def removeLast(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head = self.tail = None
            self.size = 0
        else:
            temp = self.head
            i = 0
            while i < self.size - 2:
                temp = temp.next
                i += 1

            self.tail = temp
            self.tail.next = None
            self.size -= 1
           
    def reverseDI(self):
        left=0
        right=self.size-1
        while(left<right):
            temp1 = self.getNodeAt(left)
            temp2 = self.getNodeAt(right)
            temp = temp1.data
            temp1.data = temp2.data
            temp2.data = temp
            left+=1
            right-=1
            
    def reversePI(self):
        if self.size <= 1:
            return

        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        temp = self.head
        self.head = self.tail
        self.tail = temp


class LLToStackAdapter:
    def __init__(self):
        self.lst = LinkedList()
        
    def size(self):
        #write your code here
        return self.lst.size
        
    def push(self,val):
        #write your code here
        return self.lst.addFirst(val)
        
    def pop(self):
        #write your code here
        if self.lst.size == 0:
            print("Stack is empty")
        else:
            return self.lst.removeFirst()

    def top(self):
        #write your code here
        if self.lst.size == 0:
            print("Stack is empty")
        else:
            return self.lst.getFirst()
            
s=LLToStackAdapter()
while True:
    cmd=input().split(" ")
    if "push" in cmd[0]:
        val=int(cmd[1])
        s.push(val)
        
    elif "pop" in cmd[0]:
        ans=s.pop()
        if(ans!=-1):
            print(ans)
            
    elif "top" in cmd[0]:
        ans=s.top()
        if(ans!=-1):
            print(ans)
            
    elif "size" in cmd[0]:
        print(s.size())
        
    elif "quit" in cmd[0]:
        break