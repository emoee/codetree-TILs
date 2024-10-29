numbers = list(map(int, input().split()))
numbers.sort()

from itertools import combinations

for a, b, c in combinations(numbers, 3):
    array = [a, b, c]
    array.append(a+b)
    array.append(a+c)
    array.append(b+c)
    array.append(a+b+c)

    array.sort()

    if array == numbers:
        print(a, b, c)
        break