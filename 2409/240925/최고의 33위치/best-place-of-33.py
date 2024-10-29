n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def getCoins(row1, row2, col1, col2):
    coins = 0
    for row in range(row1, row2):
        for col in range(col1, col2):
            coins += grid[row][col]

    return coins

maxCoins = 0
for i in range(n-2):
    for j in range(n-2):
        if i+3 <= n and j+3 <= n:
            maxCoins = max(maxCoins, getCoins(i, i+3, j, j+3))

print(maxCoins)