n, k = map(int, input().split())

numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

result = 0
for i in range(n-1):
    value = numbers[i]
    count = 1

    for j in range(i+1, n):
        if abs(value - numbers[j]) <= k:
            count += 1
        else:
            break
    result = max(result, count)

print(result)