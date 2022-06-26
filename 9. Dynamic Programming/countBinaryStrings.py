def countBinaryString(n):
    countForZero = 0
    countForOne = 0

    valueOfzero = 1
    valueOfOne = 1

    for i in range(2, n+1):
        countForOne = valueOfOne + valueOfzero
        countForZero = valueOfOne
        valueOfOne = countForOne
        valueOfzero = countForZero

    totalbinaryStrings = countForOne + countForZero

    return totalbinaryStrings


print(countBinaryString(5))