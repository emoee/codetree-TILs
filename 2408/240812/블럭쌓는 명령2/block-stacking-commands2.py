n, k = map(int, input().split())

board = [0]*n
for i in range(k):
    a, b = map(int, input().split())
    for j in range(a-1, b):
        board[j] += 1
    
print(max(board))