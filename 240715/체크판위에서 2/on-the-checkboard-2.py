r, c = map(int, input().split())
board= [[0]*c for _ in range(r)]

for i in range(r):
    board[i] = (list(map(str, input().split())))

# r은 세로, c 가 가로 

count = 0
for i in range(1, r):
    for j in range(1, c):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if board[0][0] != board[i][j] and board[i][j] != board[k][l] and board[k][l] != board[r-1][c-1]:
                    count += 1

print(count)