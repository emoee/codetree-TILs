n = int(input())

order = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
result = 0
    
for i in range(n):
    for j in range(i+1, n):
        board = [0] * 101
        value = True
        for k in range(n):
            if k != i and k != j:
                for l in range(n):
                    if i == l or j == l or k == l:
                        continue
                    x, y = order[l]
                    for b in range(x, y+1):
                        board[b] += 1
                        if board[b] > 1:
                            value = False
                
                if value == True:
                    result += 1

print(result)