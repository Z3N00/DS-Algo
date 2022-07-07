
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
            self.size += 1
        else:
            self.tail.next = temp
            self.tail = temp
            self.size += 1

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def removeFirst(self):
        if self.size == 0:
            print(
                "List is empty")
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
            print(
                "Invalid arguments")
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

l1 = LinkedList()
while True:
    cmd = input().split(" ")
    if "addLast" in cmd[0]:
        val = int(cmd[1])
        l1.addLast(val)

    elif "getFirst" in cmd[0]:
        ans = l1.getFirst()
        if (ans != -1):
            print(ans)

    elif "getLast" in cmd[0]:
        ans = l1.getLast()
        if (ans != -1):
            print(ans)

    elif "getAt" in cmd[0]:
        idx = int(
            cmd[1])
        ans = l1.getAt(idx)
        if (ans != -1):
            print(ans)

    elif "removeFirst" in cmd[0]:
        l1.removeFirst()

    elif "addFirst" in cmd[0]:
        val = int(cmd[1])
        l1.addFirst(val)

    elif "quit" in cmd[0]:
        break

    elif "display" in cmd[0]:
        l1.display()

    elif "size" in cmd[0]:
        print(l1.size)

    elif "addAt" in cmd[0]:
        idx = int(cmd[1])
        val = int(cmd[2])
        l1.addAt(idx, val)
