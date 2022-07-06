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

    def size(self):
        return self.size

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
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
        # write your code here
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            return self.head.data

    def getLast(self):
        # write your code here
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            return self.tail.data
        
    def getAt(self, idx):
        # write your code here
        if self.size == 0:
            print("List is empty")
            return -1
        elif idx < 0 or idx > self.size:
            print("Invalid arguments")
            return -1

        else:
            temp = self.head
            i = 1
            while i < idx:
                temp = temp.next
                i += 1
            return temp.data



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
        idx = int(cmd[1])
        ans = l1.getAt(idx)
        if (ans != -1):
            print(ans)

    elif "removeFirst" in cmd[0]:
        l1.removeFirst()

    elif "quit" in cmd[0]:
        break
