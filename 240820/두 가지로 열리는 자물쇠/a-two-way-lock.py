n = int(input())

a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

def getNumber(n, t):
    return {(t-2-1)%n+1, (t-1-1)%n+1, (t+1-1)%n+1, (t+2-1)%n+1, t}

def getNumbers(x, y, z, n):
    A = getNumber(n, x)
    B = getNumber(n, y)
    C = getNumber(n, z)
    return A, B, C

def getNumberSame(x, y):
    return x&y

setA, setB, setC = getNumbers(a, b, c, n)
setD, setE, setF = getNumbers(d, e, f, n)

same1 = getNumberSame(setA, setD)
same2 = getNumberSame(setB, setE)
same3 = getNumberSame(setC, setF)

countA = len(setA) * len(setB) * len(setC)
countD = len(setD) * len(setE) * len(setF)
same = len(same1) * len(same2) * len(same3)

print(countA+countD-same)