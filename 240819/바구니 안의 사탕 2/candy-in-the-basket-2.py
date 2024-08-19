n, k = map(int, input().split())

board = [0] * 101
for i in range(n):
    a, b = map(int, input().split())
    board[b] += a

maxCandy = 0
for i in range(k, 101-k):
    candy = 0
    for j in range(i-k, i+k+1):
        candy += board[j]

    maxCandy = max(candy, maxCandy)

print(maxCandy)