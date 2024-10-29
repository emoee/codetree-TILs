n = int(input())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

result = [0] * 101

count = 0
result[0] = listA[0]
for i in range(n-1):
    for k in range(100000):
        if k == listB[i]:
            count += result[i] - k
            result[i+1] = listA[i+1] + (result[i] - k)
            break

print(count)