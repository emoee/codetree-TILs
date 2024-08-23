n, m = map(int, input().split())

numbers = list(map(int, input().split()))

result = 0
for i in range(n):
    value = 0
    start = i
    for j in range(m):
        value += numbers[start]
        start = numbers[start] - 1
    result = max(result, value)

print(result)