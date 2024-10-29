n, c, g, h = map(int, input().split())
MAXV = 1000
order = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def check(number, ta, tb):
    if number < ta:
        return c
    elif number <= tb:
        return g
    else:
        return h

def allCheck(t):
    total = 0
    for x, y in order:
        total += check(t, x, y)
    return total

result = 0
for i in range(MAXV+1):
    result = max(result, allCheck(i))

print(result)