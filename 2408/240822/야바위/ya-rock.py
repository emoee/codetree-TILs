n = int(input())


order = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

result = 0
for i in range(n):
    board = [0] * (n+1)
    board[i+1] = 1
    count = 0
    for a, b, c in order:
        board[a], board[b] = board[b], board[a]
        if board[c] == 1:
            count += 1
    
    result = max(result, count)

print(result)