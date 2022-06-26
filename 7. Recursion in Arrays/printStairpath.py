def printStairpath(ques, ans):

    if(ques==0):
        print(ans)
        return
    if(ques<0):
        return

    printStairpath(ques-1, "1" + ans)
    printStairpath(ques-2, "2" + ans)
    printStairpath(ques-3, "3" + ans)



printStairpath(3, "")