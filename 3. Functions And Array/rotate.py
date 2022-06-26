a = [1, 2, 3, 4, 5]
k = 3
def reverse(a, start, end):
    while(start < end):
        temp = a[end]
        a[end] = a[start]
        a[start] = temp
        start+=1
        end-=1
    return a

def rotate(a, k):
    
    if(k<0):
        k = k + len(a)
    k = k%len(a)
    #part1
    s1 = 0
    e1 = len(a) - k - 1
    reverse(a, s1, e1)
    #part2
    s2 = len(a) - k
    e2 = len(a) - 1
    reverse(a, s2, e2)
    #all
    s = 0
    e = len(a) - 1
    ans = reverse(a, s, e)
    print(ans)

rotate(a, k)