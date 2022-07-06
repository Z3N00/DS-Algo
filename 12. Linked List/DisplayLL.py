class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def AddLast(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
            self.size += 1
            return
        laste = self.head
        while (laste.next):
            laste = laste.next
            laste.next = NewNode
            self.tail = laste.next
            self.size += 1

    def display(self):
    #write your code here
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next

                                                
    def testList(self) :
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

            print(self.size)

            if  self.size > 0 :

                print(self.tail.data)

                l1 = SLinkedList()
                while 1 > 0 :
                    str = input()
                    if str[0] == 'q':
                        break
                    elif str[0] == 'a':
                        val = int(str[-3] + str[-2])

                        l1.AddLast(val)

                    elif str[0] == 'd':
                        l1.display()

                    elif str[0] == 's':

                        print(l1.size)