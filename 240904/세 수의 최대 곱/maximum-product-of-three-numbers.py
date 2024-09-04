from itertools import combinations
n = int(input())

numbers = list(map(int, input().split()))

result = numbers[0] * numbers[1] * numbers[2]
for a, b, c in combinations(numbers, 3):
    result = max(result, a*b*c)

print(result)