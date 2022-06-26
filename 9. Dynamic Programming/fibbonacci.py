

def main():
    n =  10 #int(input())
    size = n + 1
    qb = [0]*size
    fibn = fibMemorized(n, qb)

    print(fibn)



def fib(n):

    if(n==0 or n==1):
        return n

    fibnm1 = fib(n-1)
    fibnm2 = fib(n-2)

    fibn = fibnm1 + fibnm2
    
    return fibn


def fibMemorized(n, qb):
    if(n==0 or n==1):
        return n
    if(qb[n]!= 0):
        return qb[n]

    fibnm1 = fibMemorized(n-1, qb)
    fibnm2 = fibMemorized(n-2, qb)

    fibn = fibnm1 + fibnm2
    qb[n] = fibn
    return fibn


main()