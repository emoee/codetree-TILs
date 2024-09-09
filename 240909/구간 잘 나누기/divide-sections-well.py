n, m = map(int, input().split())
numbers = list(map(int, input().split()))

from itertools import combinations 

maxValue = 0
k = n//m
for i in range(0, n, k):
    number = 0
    for j in range(i, (i+k)): 
        number += numbers[j]
    
    maxValue = max(maxValue, number)

print(maxValue)