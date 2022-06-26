def maxSumNonAdjacentElement():
    n = int(input())

    arr = [int(input()) for i in range(n)]


    inc = arr[0]
    exc = 0
    for i in range(1, n):
        newinc = exc + arr[i]
        newexc = max(inc, exc)

        inc = newinc
        exc = newexc


    print(max(inc, exc))


maxSumNonAdjacentElement()