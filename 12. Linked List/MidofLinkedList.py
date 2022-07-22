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
       
    def kthFromLast(self, k):
        # write your code here
        if self.size == 0:
            print("List is Empty")
            return
        slow = self.head
        fast = self.head
    
        for i in range(k):
            fast = fast.next
        while fast != self.tail:
            slow = slow.next
            fast = fast.next
        
        return slow.data
    
    def mid(self):
        slow = self.head
        fast = self.head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow.data
        
l1 = LinkedList()
while True:
    cmd=input().split(" ")
    if "quit" in cmd[0]:
        break
    elif "addLast" in cmd[0]:
        val=int(cmd[1])
        l1.addLast(val)
    elif "size" in cmd[0]:
        print(l1.size)
    elif "display" in cmd[0]:
        l1.display()
    elif "removeFirst" in cmd[0]:
        l1.removeFirst()
    elif "getFirst" in cmd[0]:
        ans=l1.getFirst()
        if(ans!=-1):
            print(ans)
    elif "getLast" in cmd[0]:
        ans=l1.getLast()
        if(ans!=-1):
            print(ans)
    elif "getAt" in cmd[0]:
        idx=int(cmd[1])
        ans=l1.getAt(idx)
        if(ans!=-1):
            print(ans)
    elif "addFirst" in cmd[0]:
        val=int(cmd[1])
        l1.addFirst(val)
    elif "addAt" in cmd[0]:
        idx=int(cmd[1])
        val=int(cmd[2])
        l1.addAt(idx,val)
    elif "removeLast" in cmd[0]:
        l1.removeLast()
    elif "removeAt" in cmd[0]:
        idx=int(cmd[1])
        l1.removeAt(idx)
    elif "reverseDI" in cmd[0]:
        l1.reverseDI()
    elif "reversePI" in cmd[0]:
        l1.reversePI()
    elif "kthFromEnd" in cmd[0]:
        idx=int(cmd[1])
        print(l1.kthFromLast(idx));
    elif "mid" in cmd[0]:
        print(l1.mid())