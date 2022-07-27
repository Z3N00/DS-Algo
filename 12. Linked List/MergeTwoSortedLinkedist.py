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
            self.head = temp
            self.tail = temp
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

#get node at

    def __getNodeAt(self, idx):
        temp = self.head
        i = 0
        while i < idx:
            temp = temp.next
            i += 1
        return temp

# mid of a linkedlist

    def mid(self):
        f = self.head
        s = self.head

        while f.next is not None and f.next.next is not None:
            f = f.next.next
            s = s.next

        return s.data

# merge two sorted linkedlist

    def mergeTwoSortedLists(self,l1, l2):

       #rite your code here
        p1 = l1.head
        p2 = l2.head
        l3 = LinkedList()
        
        while p1 != None and p2 != None:
            if p1.data < p2.data:
                l3.addLast(p1.data)
                p1 = p1.next
            else:
                l3.addLast(p2.data)
                p2 = p2.next

        while p1 != None:
            l3.addLast(p1.data)
            p1 = p1.next

        while p2 != None:
            l3.addLast(p2.data)
            p2 = p2.next

        return l3

       
n = int(input())
l1 = LinkedList()
values1 = input().split(" ")
for i in range(n):
    l1.addLast(int(values1[i]))

m = int(input())
l2 = LinkedList()
values2 = input().split(" ")
for i in range(m):
    l2.addLast(int(values2[i]))

l3 = LinkedList()
ans = l3.mergeTwoSortedLists(l1, l2);

ans.display()
l1.display()
l2.display()