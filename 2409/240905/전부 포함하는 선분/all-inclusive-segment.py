n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

result = 200
for i in range(n):
    x1, x2 = 100, 0
    for j in range(n):
        if lines[i] == lines[j]:
            continue
        x1 = min(x1, lines[j][0])
        x2 = max(x2, lines[j][1])

    result = min(result, abs(x2-x1))

print(result)