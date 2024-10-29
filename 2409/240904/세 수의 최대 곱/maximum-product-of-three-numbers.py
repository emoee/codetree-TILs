from itertools import combinations
n = int(input())

numbers = list(map(int, input().split()))
result = numbers[0] * numbers[1] * numbers[2]
numbers.sort()

a = numbers[0] * numbers[1] * numbers[-1]
b = numbers[-1] * numbers[-2] * numbers[-3]

result = max(result, a, b)
print(result)