n = int(input())
array = list(map(str, input().split()))

count = 0
result = array.copy()
result.sort()

for i in range(1, n):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
            count += 1
    if result == array:
        break
print(count)