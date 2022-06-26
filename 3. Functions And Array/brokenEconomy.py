n = 10
a = [1, 5, 10, 15, 22, 33, 40, 42, 55, 66]
d = 34

floor = 0
ceil = 0

start = 0
end = n-1


while(start<=end):
    mid = int((start + end) / 2)
    if(d>a[mid]):
        start = mid + 1
        floor = a[mid]
        ceil = a[mid + 1]
    elif(d<a[mid]):
        end = mid - 1
        floor = a[mid - 1]
        ceil = a[mid]
    elif(d == a[mid]):
        print(a[mid])
        break
    if(start==end):
        print(floor, ceil)
