n = int(input())
A = list(map(int, input().split()))

result = []
for i, a in enumerate(A):
    result.append(a)
    result.sort()
    if (i+1)%2 == 0:
        continue
    print(result[i//2], end= " ")