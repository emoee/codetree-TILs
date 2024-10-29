from itertools import combinations, permutations

numbers = list(map(int, input().split()))

numbers.sort()
n = len(numbers)

result = ()
for i in combinations(numbers, 4):
    array = list(i)
    for j in combinations(i, 2):
        array.append(j[0] + j[1])

    for k in combinations(i, 3):
        array.append(k[0] + k[1] + k[2])

    array.append(sum(i))
    array.sort()

    if numbers == array:
        result = i
        break

for i in range(4):
    print(result[i], end=' ')