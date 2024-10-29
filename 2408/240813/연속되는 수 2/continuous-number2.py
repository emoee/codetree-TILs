n = int(input())

line = [int(input()) for _ in range(n)]
cnt = 0
result = 0

for i in range(n):
    if i == 0 or line[i-1] == line[i]:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)

print(result)