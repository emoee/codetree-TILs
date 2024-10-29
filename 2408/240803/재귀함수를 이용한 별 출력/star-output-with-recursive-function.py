n = int(input())

def printStar(number):
    print("*" * number)
    if number == n:
        return 0
    return printStar(number+1)

printStar(1)