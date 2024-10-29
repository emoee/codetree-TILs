n, k = map(int, input().split())

board = []

for i in range(n):
    board.append(int(input()))

result = -1
for i in range(n-1):
    for j in range(i+1, n):
        if board[i] == board[j] and j - i <= k:
            result = max(result, board[i])
                
print(result)