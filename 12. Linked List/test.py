class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _size(self):
        print(f"size of Linked list: {self.size}")

    def addLast(self, val):
        node = Node(val)

        if self.size == 0:
            self.head = self.tail = node
            self.size += 1

        else:
            temp = self.tail
            temp.next = node
            self.tail = node
            self.size += 1

    def addFirst(self, val):
        node = Node(val)
        if self.size == 0:
            self.head = self.tail = node
            self.size += 1
        else:
            temp = self.head
            self.head = node
            node.next = temp
            self.size += 1

    def addAt(self,idx, val):
        node = Node(val)
        if idx < 0 or idx > self.size:
            print("Invalid Argument")
        elif idx == 0:
            self.addFirst(val)
        elif idx == self.size:
            self.addLast(val)
        else:
            temp = self.head
            i = 0
            while i < idx - 1:
                temp = temp.next
                i += 1

            node.next = temp.next
            temp.next = node
            self.size += 1

    def giveAt(self, idx):
        if self.size == 0:
            print("List is empty")
            
        elif idx < 0 or idx > self.size:
            print("Invalid arguments")
            
        else:
            temp = self.head
            i = 0
            while i < idx:
                temp = temp.next
                i += 1
            print(temp.data)

    def removeFirst(self):
        self.head = self.head.next
        self.size -= 1

    def removeLast(self):
        #write your code here
        temp = self.head
        i = 0
        while i < self.size - 2:
            temp = temp.next
            i += 1
        self.tail = temp
        temp.next = None
        self.size -= 1

    def removeAt(self, idx):
    #write your code here
        if idx < 0 or idx > self.size:
            print("Invalid argument")
        elif idx == 0:
            self.removeFirst()
        elif idx == self.size:
            self.removeLast()
        else:
            temp = self.head
            i = 0
            while i < idx-1:
                temp = temp.next
                i += 1
            temp.next = temp.next.next
            self.size -= 1

    def display(self):
        printval = self.head
        while printval:
            print(printval.data, "->", end=" ")
            printval = printval.next
        print()


li = LinkedList()
i = 10
while i <= 20:
    li.addLast(i)
    i += 1

#li.addFirst(100)
#li.addAt(3, 200)
#li.giveAt(12)
#li.removeFirst()
li.display()
li._size()
print("----------------------------------")
li.removeAt(10)
li.display()
li._size()
