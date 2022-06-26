def numWays(n: int, k: int):
        #write your code here
        same = k*1
        diff = k*(k-1)
        total = same + diff

        for i in range(3, n+1):
            same = diff * 1
            diff = total*(k-1)
            total = same + diff
        return total


n=int(input())
k=int(input())

print(numWays(n,k))