n = 5
arr = [3, 1, 0, 7, 5]
max = max(arr)


for i in range(n):
    for floor in arr:
        if(floor >= max-i):
            print("*\t", end="")
        else:
            print("\t", end="")    

    print()