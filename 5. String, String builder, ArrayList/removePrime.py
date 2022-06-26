n = 4
al = [3, 12, 13, 15]

for i in range(len(al)-1, -1, -1):
    div = 2
    while(div*div<=al[i]):
        if(al[i]%div==0):
            break
        div += 1
    if(div*div > al[i]):
        al.remove(al[i])
print(al)