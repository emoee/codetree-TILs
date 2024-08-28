n, k = map(int, input().split())
arr = [
    int(input()) for _ in range(n)
]
result = [0] * 1000000

def in_range(x):
    return 0 <= x < n

for i in range(n):
    b = arr[i]
    for j in range(i+1, i+k+1):
        if in_range(j) and b == arr[j]:
            result[b] += 1
    
maxValue = max(result)
index = 0

if maxValue == 0:
    index = 0
else:
    for i in range(len(result)):
        if maxValue == result[i]:
            index = i

print(index)