n, m, k = map(int, input().split())
gamelist = list(map(int, input().split()))
board = [1 for _ in range(k)]
ans = 0

def calc():
    score = 0
    for b in board:
        score += (b >= m)
    return score

def find(cnt):
    global ans
    ans = max(ans, calc())

    if cnt == n:
        return
    print(board, ans)
    for i in range(k):
        print(board)
        if board[i] >= m:
            continue
        board[i] += gamelist[cnt]
        find(cnt+1)
        board[i] -= gamelist[cnt]

find(0)
print(ans)