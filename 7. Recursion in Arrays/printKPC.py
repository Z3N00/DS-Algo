DIC = {
    "0": ".;",
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tu",
    "8": "vwx",
    "9": "yz"
}

def KPC(ques, ans):
    if(len(ques)==0):
        print(ans)
        return
    ch = ques[0] #7
    roq = ques[1:] #8...
    
    
    codeforch = DIC[ch]
    for i in range(len(codeforch)):
        cho  = codeforch[i]
        
        KPC(roq, ans + cho)
            

s = "78"
KPC(s, "")