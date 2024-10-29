n, k = map(int, input().split())

board = [0] * 401 # k의 범위는 200이니까 +-해서 400...
for i in range(n):
    a, b = map(int, input().split())
    board[b] += a

maxCandy = 0

for i in range(k, 401-k):
    candy = 0
    for j in range(i-k, i+k+1):
        candy += board[j]

    maxCandy = max(candy, maxCandy)

print(maxCandy)