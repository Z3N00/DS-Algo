def printTargetSubSet(arr, indx, set, sos, tar):

    if(indx >= len(arr)):
        if(sos == tar):
            print(set + ".")
        return

    printTargetSubSet(arr, indx+1, set + str(arr[indx]) + ',', sos+arr[indx], tar)
    printTargetSubSet(arr, indx+1, set, sos, tar)













if  __name__ == "__main__":
    
    arr = [10, 20, 30]
    printTargetSubSet(arr, 0, "", 0, 30)