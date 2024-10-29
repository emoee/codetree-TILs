n = int(input())
A = list(input())

countC = 0
countCO = 0
countCOW = 0

for c in A:
    if c == 'C':
        countC += 1
    elif c == 'O':
        countCO += countC
    elif c == 'W':
        countCOW += countCO

print(countCOW)