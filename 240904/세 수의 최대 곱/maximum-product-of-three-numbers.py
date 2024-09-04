from itertools import combinations
n = int(input())

numbers = list(map(int, input().split()))

result = 0
for a, b, c in combinations(numbers, 3):
    result = max(result, a*b*c)

print(result)