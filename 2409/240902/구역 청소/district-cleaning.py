a, b = map(int, input().split())
c, d = map(int, input().split())

result = [0] * 101

for i in range(a, b):
    result[i] = 1
for i in range(c, d):
    result[i] = 1

print(sum(result))