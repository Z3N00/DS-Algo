from tkinter import N


def arrangeBuildings():
    n = int(input())
    
    countofBuilding = 0
    countofSpace = 0
    valueofBuilding = 1
    valueofSpace = 1
    for i in range(2, n+1):
        countofBuilding = valueofSpace
        countofSpace = valueofBuilding + valueofSpace

        valueofBuilding = countofBuilding
        valueofSpace = countofSpace

    print((countofBuilding+countofSpace)**2)



arrangeBuildings()