n = int(input())
line = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
line.sort()

value = 40001
for i in range(n):
    x, x2, y, y2 = 40001, 0, 40001, 0
    for j in range(n):
        if i == j:
            continue
        
        x = min(x, line[j][0])
        x2 = max(x2, line[j][0])

        y = min(y, line[j][1])
        y2 = max(y2, line[j][1])

    row = x2-x
    col = y2-y

    value = min(value, row*col)

print(value)