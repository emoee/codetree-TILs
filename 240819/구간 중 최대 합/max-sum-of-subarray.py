n, k = map(int, input().split())
numbers = list(map(int, input().split()))

maxValue = 0
for i in range(n-k+1):
    value = 0
    for j in range(i, i+k):
        value += numbers[j]
    maxValue = max(maxValue, value)

print(maxValue)