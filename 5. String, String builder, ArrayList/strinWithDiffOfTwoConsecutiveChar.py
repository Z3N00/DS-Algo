# ord
s = "abecd"

nl = []

for i in range(len(s)-1):
    
    value = ord(s[i+1]) - ord(s[i])
    nl.append(s[i])
    nl.append(str(value))
        
nl.append(s[i+1])
ns = "".join(nl)
print(ns)