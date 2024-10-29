def changeNumber(a, b):
    return b, a

n, m = map(int, input().split())

a, b = changeNumber(n,m)
print(a, b)