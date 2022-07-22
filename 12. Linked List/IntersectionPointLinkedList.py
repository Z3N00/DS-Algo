class Node(object):

    def __init__(self):
        self.data = 0
        self.next = None


class LinkedList(object):

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

    def size(self):
        return self.size

    def display(self):
        temp = head
        while temp is not None:
            print(temp.data + " ", end = '')
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

    def addAt(self, idx, val):
        if idx < 0 or idx > size:
            print("Invalid arguments")
        elif idx == 0:
            addFirst(val)
        elif idx == size:
            addLast(val)
        else:
            node = Node()
            node.data = val

            temp = head
            i = 0
            while i < idx - 1:
                temp = temp.next
                i += 1
            node.next = temp.next

            temp.next = node
            size += 1

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

    def removeAt(self, idx):
        if idx < 0 or idx >= size:
            print("Invalid arguments")
        elif idx == 0:
            removeFirst()
        elif idx == size - 1:
            self.removeLast()
        else:
            temp = head
            i = 0
            while i < idx - 1:
                temp = temp.next
                i += 1

            temp.next = temp.next.next
            size -= 1

    def getNodeAt(self, idx):
        temp = self.head
        i = 0
        while i < idx:
            temp = temp.next
            i += 1
        return temp

    def reverseDI(self):
        li = 0
        ri = size - 1
        while li < ri:
            left = self.__getNodeAt(li)
            right = self.__getNodeAt(ri)

            temp = left.data
            left.data = right.data
            right.data = temp

            li += 1
            ri -= 1

    def reversePI(self):
        if size <= 1:
            return

        prev = None
        curr = head
        while curr is not None:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        temp = head
        head = tail
        tail = temp

    def kthFromLast(self, k):
        slow = head
        fast = head
        i = 0
        while i < k:
            fast = fast.next
            i += 1

        while fast is not tail:
            slow = slow.next
            fast = fast.next

        return slow.data

    def mid(self):
        f = head
        s = head

        while f.next is not None and f.next.next is not None:
            f = f.next.next
            s = s.next

        return s.data

    @staticmethod
    def mergeTwoSortedLists(l1, l2):
        ml = LinkedList()

        one = l1.head
        two = l2.head
        while one is not None and two is not None:
            if one.data < two.data:
                ml.addLast(one.data)
                one = one.next
            else:
                ml.addLast(two.data)
                two = two.next

        while one is not None:
            ml.addLast(one.data)
            one = one.next

        while two is not None:
            ml.addLast(two.data)
            two = two.next

        return ml

    @staticmethod
    def midNode(head, tail):
        f = head
        s = head

        while f is not tail and f.next is not tail:
            f = f.next.next
            s = s.next

        return s

    @staticmethod
    def mergeSort(head, tail):
        if head is tail:
            br = LinkedList()
            br.addLast(head.data)
            return br

        mid = midNode(head, tail)
        fsh = mergeSort(head, mid)
        ssh = mergeSort(mid.next, tail)
        sl = mergeTwoSortedLists(fsh, ssh)
        return sl

    def removeDuplicates(self):
        res = LinkedList()

        while self.size() > 0:
            val = self.getFirst()
            self.removeFirst()

            if res.size() == 0 or val != res.tail.data:
                res.addLast(val)

        self.head = res.head
        self.tail = res.tail
        self.size = res.size

    def oddEven(self):
        odd = LinkedList()
        even = LinkedList()

        while self.size > 0:
            val = self.getFirst()
            self.removeFirst()

            if val % 2 == 0:
                even.addLast(val)
            else:
                odd.addLast(val)

        if odd.size > 0 and even.size > 0:
            odd.tail.next = even.head

            self.head = odd.head
            self.tail = even.tail
            self.size = odd.size + even.size
        elif odd.size > 0:
            self.head = odd.head
            self.tail = odd.tail
            self.size = odd.size
        elif even.size > 0:
            self.head = even.head
            self.tail = even.tail
            self.size = even.size

    def kReverse(self, k):
        prev = None

        while self.size > 0:
            curr = LinkedList()

            if self.size >= k:
                i = 0
                while i < k:
                    val = self.getFirst()
                    self.removeFirst()
                    curr.addFirst(val)
                    i += 1
            else:
                sz = self.size
                i = 0
                while i < sz:
                    val = self.getFirst()
                    self.removeFirst()
                    curr.addLast(val)
                    i += 1

            if prev is None:
                prev = curr
            else:
                prev.tail.next = curr.head
                prev.tail = curr.tail
                prev.size += curr.size

        self.head = prev.head
        self.tail = prev.tail
        self.size = prev.size

    def __displayReverseHelper(self, node):
        if node is None:
            return
        self.__displayReverseHelper(node.next)
        print(node.data + " ", end = '')

    def displayReverse(self):
        self.__displayReverseHelper(head)
        print()

    def __reversePRHelper(self, node):
        if node is tail:
            return
        self.__reversePRHelper(node.next)
        node.next.next = node

    def reversePR(self):
        self.__reversePRHelper(head)
        temp = head
        head = tail
        tail = temp
        tail.next = None
        
    
    def findIntersection(self,one,two):

        t1 = one.head
        t2 = two.head

        delta = one.size - two.size
        if one.size > two.size:
            for i in range(delta):
                t1 = t1.next
        else:
            for i in range(delta):
                t2 = t2.next
        
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
        
        return t1.data


a_llist1 = LinkedList()

n = int(input())
values = list(map(int,input().split(" ")))
for i in range(n):
    a_llist1.addLast(values[i])

a_llist2 = LinkedList()

m = int(input())
values = list(map(int,input().split(" ")))
for i in range(m):
    a_llist2.addLast(values[i])

li = int(input())
di = int(input())

if li == 1:
    n = a_llist1.getNodeAt(di)

    if a_llist2.size > 0:
        a_llist2.tail.next = n
    else:
        a_llist2.head = n

    a_llist2.tail = a_llist1.tail
    a_llist2.size += a_llist1.size - di
else:
    n = a_llist2.getNodeAt(di)

    if a_llist1.size > 0:
        a_llist1.tail.next = n
    else:
        a_llist1.head = n

    a_llist1.tail = a_llist2.tail
    a_llist1.size += a_llist2.size - di

inter = a_llist1.findIntersection(a_llist1, a_llist2)
print(inter)