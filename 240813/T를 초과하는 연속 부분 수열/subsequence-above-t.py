n, t = map(int, input().split())

numbers = list(map(int, input().split()))

result, cnt = 1, 1
for i in range(n):
    if numbers[i-1] > t and numbers[i] > t:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)

print(result)