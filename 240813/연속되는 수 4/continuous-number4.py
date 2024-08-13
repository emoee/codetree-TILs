n = int(input())

number = []

for i in range(n):
    number.append(int(input()))

result, cnt = 1, 1
for i in range(1, n):
    if number[i-1] < number[i]:
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)


print(result)