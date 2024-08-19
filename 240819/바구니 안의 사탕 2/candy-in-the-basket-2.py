n, k = map(int, input().split())

board = [0] * 301
for i in range(n):
    a, b = map(int, input().split())
    board[b] += a

maxCandy = 0

for i in range(k, 301-k):
    candy = 0
    for j in range(i-k, i+k+1):
        candy += board[j]
    # print(i, k, candy)
    maxCandy = max(candy, maxCandy)

print(maxCandy)