numbers = list(map(int, input().split()))

def diff(i, j, k):
    sumA = numbers[i] + numbers[j] + numbers[k]
    sumB = sum(numbers) - sumA
    return abs(sumA - sumB)

result = 1000000
for i in range(4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            result = min(result, diff(i, j, k))

print(result)