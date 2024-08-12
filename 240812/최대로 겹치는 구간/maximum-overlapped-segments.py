n = int(input())

line = [0] * 200
for i in range(n):
    a, b = map(int, input().split())
    a, b = a+100, b+100
    for j in range(a+1, b):
        line[j] += 1

print(max(line))