n, k = map(int, input().split())

MAXV = 1000
order = [0] * (MAXV * MAXV + 1)
for i in range(n):
    l, c = map(str, input().split())
    if c == 'G': 
        order[int(l)] = 1
    elif c == 'H':
        order[int(l)] = 2

maxValue = 0
for i in range(MAXV-k+1):
    count = 0
    for j in range(i, i+k+1):
        count += order[j]
    maxValue = max(maxValue, count)

print(maxValue)