n = int(input())

line = [int(input()) for _ in range(n)]

MAXV = max(line)
cnt = 0

result = 0
for i in range(n):
    if MAXV == line[i]:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 0
        
print(result)