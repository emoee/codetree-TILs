import sys
n = int(input())
A = (list(map(int, input().split())))

minValue = sys.maxsize
for i in range(n):
    t = A[i]
    sumA = 0
    for j in range(n):
        sumA += A[j] * abs(i-j)
    if sumA < minValue:
        minValue = sumA

print(minValue)