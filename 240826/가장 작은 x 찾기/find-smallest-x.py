n = int(input())

find = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

MINV = find[0][0]
MAXV = find[n-1][1]

result = MAXV
for i in range(MINV, MAXV+1):
    value = i
    check = True
    for a, b in find:
        value *= 2
        if a > value or value > b:
            check = False

    if check:
        result = min(result, i)

print(result)