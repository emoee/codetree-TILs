n = int(input())

def printFlower(f):
    if f == 0:
        return

    print(f, end=" ")
    printFlower(f-1)
    print(f, end=" ")
    
printFlower(n)