n, m, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

p = 0
for i in range(n):
    loop = False
    for j in range(k-1, k+m-1):
        if board[i][j] != 0:
            loop = True
            break
    if loop:
        break
    
    p = i


for b in range(k-1, k+m-1):
    board[p][b] = 1

for r in board:
    print(" ".join(map(str, r)))