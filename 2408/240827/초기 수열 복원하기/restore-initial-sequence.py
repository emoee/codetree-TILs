n = int(input())
numbers = list(map(int, input().split()))
MAXV = 1000
arr = [0] * n


for i in range(1, n+1):
    arr[0] = i

    for j in range(1, n):
        arr[j] = numbers[j-1] - arr[j-1]


    satisfied = True
    exist = [False] * (MAXV + 1)

    for k in range(n):
        if arr[k] <= 0 or arr[k] > n:
            satisfied = False
        else:
            if exist[arr[k]]:
                satisfied = False
            exist[arr[k]] = True

    if satisfied:
        for l in range(n):
            print(arr[l], end=' ')
        break