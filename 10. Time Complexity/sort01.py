def swap(arr, i, j):
    print("Swapping index" , i , "and index" , j);
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;


def sort01(arr):
    # write your code here
    i = 0
    j = 0
    while(i<len(arr)):
        
        if(arr[i] == 1):
            i += 1
        elif(arr[i] == 0):
            swap(arr, i, j)
            i += 1
            j += 1



def Display(arr):
    for i in arr:
        print(i);
    

def main():
#  n = int(input());
  arr = [0, 1, 0, 1, 0];
  
#   for i in range(0, n):
#     ele = int(input());
#     arr.append(ele);

  sort01(arr);
  Display(arr);
  
if __name__ == "__main__":
    main();