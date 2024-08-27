n, k = map(int, input().split())
arr = [
    int(input()) for _ in range(n)
]
result = [0] * 1000000

for i in range(n):
    for j in range(i+1, n):
        value = 0
        if (arr[i] == arr[j]) and abs(i-j) <= k:
            for k in range(i, j+1):
                if arr[k] == arr[i]:
                    value += 1

        result[arr[i]] = max(result[arr[i]], value)
    

print(result.index(max(result)))