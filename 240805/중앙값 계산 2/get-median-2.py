n = int(input())
A = list(map(int, input().split()))

result = []
for a in A:
    result.append(a)
    if a%2 == 0:
        continue
    print(result[len(result)//2], end= " ")