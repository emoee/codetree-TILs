n , m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

maxValue = 0
result = []
def Choose(cnt, start):
    global maxValue

    if cnt == m:
        value = result[0]
        for j in range(1, m):
            value ^= result[j]
        maxValue = max(maxValue, value)
        return
    
    for i in range(start+1, n):
        result.append(numbers[i])
        Choose(cnt+1, i)
        result.pop()

for i in range(n):
    result.append(numbers[i])
    Choose(1, i)
    result.pop()

print(maxValue)