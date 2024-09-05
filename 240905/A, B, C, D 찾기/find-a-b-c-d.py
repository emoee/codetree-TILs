numbers = list(map(int, input().split()))
numbers.sort()

from itertools import combinations

for a, b, c, d in combinations(numbers, 4):
    array = [a,b,c,d]
    for x, y in combinations([a,b,c,d], 2):
        array.append(x+y)
    
    array.append(a+b+c)
    array.append(a+b+d)
    array.append(a+c+d)
    array.append(d+b+c)
    array.append(a+b+c+d)

    array.sort()
    if array == numbers:
        print(a, b, c, d)
        break