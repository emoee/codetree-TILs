n = int(input())
line = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
line.sort()

value = 1000*1000
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = line[i]
        x2, y2 = line[j]
        distance = ((x1-x2) * (x1-x2)) + ((y1-y2) * (y1-y2))
        value = min(value, distance)

print(value)