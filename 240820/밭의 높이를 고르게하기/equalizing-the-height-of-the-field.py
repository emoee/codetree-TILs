n, h, t = map(int, input().split())

numbers = list(map(int, input().split()))

result = 200
for i in range(n-t+1):
    sumValue = 0
    for j in range(i, i+t):
        sumValue += abs(numbers[j]-h)
    result = min(result, sumValue)

print(result)