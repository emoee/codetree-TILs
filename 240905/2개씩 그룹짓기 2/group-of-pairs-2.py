n = int(input())
numbers = list(map(int, input().split()))

from itertools import combinations

count = 2*n//n
print(count)
for a, b in combinations(numbers, count):
    print(a,b)