class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self,h,t,s):
        self.head = h
        self.tail = t
        self.size = s
        
    def addLast(self,val):
        temp = Node(val)
        if(self.size == 0):
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def display(self):
        temp=self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next
            
    left = None
    def isPalindromeHelper(self,node):
        if(node == None):
          self.left = self.head
          return True
        if(self.isPalindromeHelper(node.next) == False):
          return False
        if(node.data != self.left.data):
          return False
        self.left = self.left.next
        return True
    
    def isPalindrome(self):
        if(self.isPalindromeHelper(self.head) == True):
          print("PALINDROME")
        else:
          print("NOT PALINDROME")

    left2=None

    def __foldHelper(self, right, floor):
        if right == None:
            return
        self.__foldHelper(right.next, floor + 1)
        
        if floor > self.size/2:
            temp = self.left2.next
            self.left2.next = right
            right.next = temp
            self.left2 = temp
        elif floor == self.size/2:
            self.tail = right
            self.tail.next = None

            
    def fold(self):
        self.left2 = self.head
        self.__foldHelper(self.head, 0)
        # write your code here
        

def main():
    l = LinkedList(None,None,0)
    n = int(input())
    values = list(map(int,input().split(" ")))
    for i in range(n):
      l.addLast(values[i])
    l.display()
    print()
    first = int(input())
    last = int(input())
    l.fold()
    l.display()
    print()
    print(first,end=" ")
    l.display()
    print(last)

if __name__=="__main__":
    main()