n = int(input())

line = [int(input()) for _ in range(n)]

MAXV = max(line)
index= line.index(MAXV)

cnt = 0


for i in range(index, n):
    if MAXV == line[i]:
        cnt += 1
    else:
        break

print(cnt)