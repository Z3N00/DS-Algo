def ssq(s):
    if(len(s)==0):
        bres = []
        bres.append("")
        return bres
    ch = s[0]
    ros = s[1:]
    rres = list(ssq(ros))
    sl = []
    for rstr in rres:
        sl.append("" + rstr)
    for rstr in rres:
        sl.append(ch + rstr)

    return sl


s = "abc"

print(ssq(s))