n, m = map(int, input().split())
numbers = list(map(int, input().split()))

def findMaxValue(numbers):
    for std in range(1, 100*100+1):
        values = []
        value = numbers[0]
        for j in range(1, n):
            if value + numbers[j] > std:
                values.append(value)
                value = numbers[j]
            else:
                value += numbers[j]
        values.append(value)
    
        if len(values) <= m:
            break
    return max(values)

result = findMaxValue(numbers)
print(result)