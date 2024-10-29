n = int(input())
A = (list(map(int, input().split())))

maxValue = 0

for i in range(len(A)-2):
    for j in range(i+2, len(A)):
        if A[i] + A[j] > maxValue:
            maxValue = A[i] + A[j]

print(maxValue)