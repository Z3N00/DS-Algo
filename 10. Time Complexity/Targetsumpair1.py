from numpy import sort


def targetSumPair(arr,target):
    #write your code here
    sort_arr = sort(arr)
    i = 0
    j = len(sort_arr) - 1
    while(i!=j):
        if(sort_arr[i] + sort_arr[j] == target):
            print(sort_arr[i], sort_arr[j])
            i += 1
            l -= 1
        elif(sort_arr[i] + sort_arr[j] > target):
            j -= 1
        elif(sort_arr[i]+sort_arr[j] < target):
            i +=1

 

n=int(input());
sort_arr=[];
for i in range(0,n):
    val=int(input());
    sort_arr.append(val);
target=int(input());
targetSumPair(sort_arr,target);