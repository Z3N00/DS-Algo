n = 5
a = [1, 1, 2, 2, 2]

d = 4

start = 0
end = n-1

while(start <= end):
    if(a[start] is d and a[end] is d):
        print(start, end)
        break
    elif(a[start] == d and a[end] != d):
        end -=1
    elif(a[start]!=d and a[end]==d):
        start +=1
    elif(a[start]!=d and a[end]!=d):
        start +=1
        end -=1
    if(start==end):
        print(-1, -1)