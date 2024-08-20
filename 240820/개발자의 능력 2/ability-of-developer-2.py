from itertools import combinations

numbers = list(map(int, input().split()))
numbers.sort()

result = []
A = numbers[0] + numbers[-1]
B = numbers[1] + numbers[-2]
C = numbers[2] + numbers[-3]

result.append(A)
result.append(B)
result.append(C)
result.sort()

print(result[-1] - result[0])