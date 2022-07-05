class CustomStack:
       
    def __init__(self , cap):
        self.cap = cap
        self.tos = -1
        self.arr = []
        self.arr = [0] * cap
       
    def size(self):
        # write your code here
       return self.tos + 1

    def push(self , data):
        # write your code here
        if self.tos == len(self.arr) - 1:
            return "Stack overflow"
        else:
            self.tos +=  1
            self.arr[self.tos] = data
       
    def top(self):
        # write ur code here
        if self.tos == -1:
            print("Stack underflow")
            return -1
        return self.arr[self.tos]
       
       
   
    def pop(self):
        # write ur code here
        if self.tos == -1:
            print("Stack underflow")
            return -1
        self.tos -= 1
        return self.arr.pop()
       
       
    def display(self):
        # write ur code here
        for i in range(self.tos, -1, -1):
           print(self.arr[i], end=' ')
        


def main():
   
    n = int(input());
   
    inpStr = str(input()).split(" ")
    st = CustomStack(n)
   
    while inpStr[0] != "quit":
        if inpStr[0].strip() == "push":
            val = inpStr[1]
            st.push(val)
        elif inpStr[0].strip() == "pop":
            val = st.pop()
            if val != -1:
                print(val)
        elif inpStr[0].strip() == "top":
            val = st.top()
            if val != -1:
                print(val)
        elif inpStr[0].strip() == "size":
            print(st.size())
        elif inpStr[0].strip() == "display":
            st.display()
           
        inpStr = str(input()).split(" ")
           
   
   
   
main()