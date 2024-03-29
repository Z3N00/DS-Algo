class Node:

    def __init__(self):
        self.data = 0
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

#adding last in linkedlist

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
        
#size of linkedlist

    def size(self):
        return self.size
        
#display a linkedlist

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
        print()
        
#remove first

    def removeFirst(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = self.head.next
            self.size -= 1
#get first

    def getFirst(self):
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            return self.head.data
#get last 

    def getLast(self):
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            return self.tail.data
            
#getat in linkedlist

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

# add first in linkedlist

    def addFirst(self, val):
        temp = Node()
        temp.data = val
        temp.next = self.head
        self.head = temp

        if self.size == 0:
            self.tail = temp

        self.size += 1

# add at in linkedlist

    def addAt(self, idx, val):
        if idx < 0 or idx > size:
            print("Invalid arguments")
        elif idx == 0:
            self.addFirst(val)
        elif idx == size:
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
            size += 1

# remove last in linkedlist

    def removeLast(self):
        if size == 0:
            print("List is empty")
        elif size == 1:
            head = tail = None
            size = 0
        else:
            temp = head
            i = 0
            while i < size - 2:
                temp = temp.next
                i += 1

            tail = temp
            tail.next = None
            size -= 1

#remove at 

    def removeAt(self, idx):
        if idx < 0 or idx >= size:
            print("Invalid arguments")
        elif idx == 0:
            self.removeFirst()
        elif idx == size - 1:
            self.removeLast()
        else:
            temp = self.head
            i = 0
            while i < idx - 1:
                temp = temp.next
                i += 1

            temp.next = temp.next.next
            size -= 1

#reverse pointer recursive

    def reversePRHelper(self, node):
        #write your code here
        if node == None:
            return
        self.reversePRHelper(node.next)
        if node == self.tail:
            pass
        else:
            node.next.next = node

    def reversePR(self):
        #write your code here
        self.reversePRHelper(self.head)
        self.head.next = None
        temp = self.head
        self.head = self.tail
        self.tail = temp


# input and output

ll = LinkedList()

n = int(input())
values = list(map(int,input().split(" ")))
for i in range(n):
    ll.addLast(values[i])
            
a = int(input())
b = int(input())

ll.display()
ll.reversePR()
ll.addLast(a)
ll.addFirst(b)
ll.display()