n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def checkRow(row):
    for c in range(n):
        check = grid[row][c]
        number = 0
        for col in range(c, n):
            if check == grid[row][col]:
                number += 1
            else:
                break
            
        if number >= m:
            return True
    return False

def checkCol(col):
    for r in range(n):
        check = grid[r][col]
        number = 0
        for row in range(r, n):
            if check == grid[row][col]:
                number += 1
            else:
                break
            
        if number >= m:
            return True
    return False

seq = 0
for i in range(n):
    if checkRow(i):
        seq += 1
    if checkCol(i):
        seq += 1

print(seq)