n = int(input())
line = []

for i in range(n):
    line.append(int(input()))

result, cnt = 0, 0
for i in range(1, n):
    if line[i] > 0 and line[i-1] > 0:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)

cnt = 0
for i in range(1, n):
    if line[i] < 0 and line[i-1] < 0:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)

print(result)