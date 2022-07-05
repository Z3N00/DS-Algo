class MinStack:
       
    def __init__(self):
        self.allData = [ ]
        self.minData = [ ]
    
       
    def size(self):
        # write your code here
        return len(self.allData)
       

    def push(self , val):
        # write your code here
        if len(self.allData) == 0:
            self.allData.append(val)
            self.minData.append(val)

        elif val < self.minData[-1]:
            self.allData.append(val)
            self.minData.append(val)

        else:
            self.allData.append(val)
            

   
       
    def top(self):
        # write your code here
        if len(self.allData) == 0:
            print("Stack underflow")
            return -1
        return self.allData[-1]
       
       
    def pop(self):
        # write your code here
        if self.allData[-1] == self.minData[-1]:
            self.minData.pop()
            return self.allData.pop()
            
            
        else:
            return self.allData.pop()
        
       
       
    def minimum(self):
        # write your code here
        if len(self.minData) == 0:
            print("Stack underflow")
            return -1
        else:
            return self.minData[-1]


def main():
   
   
    inpStr = str(input()).strip().split(" ")
    st = MinStack()
   
    while inpStr[0] != "quit":
        if inpStr[0].strip() == "push":
            val = inpStr[1]
            st.push(int(val))
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
        elif inpStr[0].strip() == "min":
            val = st.minimum()
            if val != -1:
                print(val)
           
        inpStr = str(input()).strip().split(" ")
   
   
main()



