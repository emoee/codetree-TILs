n = int(input())

def printStars(s):
    if s == 0:
        return
    
    print("* " * s)
    printStars(s-1)
    print("* " * s)

printStars(n)