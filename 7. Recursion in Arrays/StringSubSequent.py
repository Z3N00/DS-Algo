def printSS(ques, ans):
    if(len(ques) == 0):
        print(ans)
        return

    ch = ques[0]
    roq = ques[1:]


    printSS(roq, ans + ch)
    printSS(roq, ans + "")







s = "yvTA"
printSS(s, "")