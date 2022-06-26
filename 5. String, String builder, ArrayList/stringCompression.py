s = "aaaaaaabbbbbbccccccddddwwqqrec"

ls1 = s[0]
ls2 = s[0]
count = 1
for i in range(len(s)):
    if s[i] == ls1[len(ls1)-1]:
        pass
       
    else:
        ls1 = ls1 + s[i]
       
for i in range(1, len(s)):
    curr = s[i]
    prev = s[i-1]
    if(curr == prev):
        count += 1
    else:
        if(count > 1):
            ls2 += str(count)
            count = 1
        ls2 += curr

if(count > 1):
    ls2 += str(count)
    count = 1
        
print(ls1, ls2)