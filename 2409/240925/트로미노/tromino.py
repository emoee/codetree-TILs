n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
BARN = 3
MODELN = 2
def inrange(x, y):
    return 0 <= x < n and 0 <= y < m

def modelTop(srow, scol): # ㄴ
    hap = 0
    breakR, breakC = srow, scol + 1
    for row in range(srow, srow+MODELN):
        for col in range(scol, scol+MODELN):
            if row == breakR and col == breakC:
                continue
            if inrange(row, col):
                hap += grid[row][col]
            else:
                return 0
    return hap
            
    
def modelLeft(srow, scol): # ㄱ 반대
    hap = 0
    breakR, breakC = srow + 1, scol + 1
    for row in range(srow, srow+MODELN):
        for col in range(scol, scol+MODELN):
            if row == breakR and col == breakC:
                continue
            if inrange(row, col):
                hap += grid[row][col]
            else:
                return 0
    return hap
            
def modelRight(srow, scol): # ㄱ
    hap = 0
    breakR, breakC = srow + 1, scol
    for row in range(srow, srow+MODELN):
        for col in range(scol, scol+MODELN):
            if row == breakR and col == breakC:
                continue
            if inrange(row, col):
                hap += grid[row][col]
            else:
                return 0
    return hap
            
def modelBottom(srow, scol): # ㄴ 반대
    hap = 0
    breakR, breakC = srow, scol
    for row in range(srow, srow+MODELN):
        for col in range(scol, scol+MODELN):
            if row == breakR and col == breakC:
                continue
            if inrange(row, col):
                hap += grid[row][col]
            else:
                return 0
    return hap
            


def barRow(srow, scol):
    hap = 0
    for row in range(srow, srow+BARN):
        if inrange(row, scol):
            hap += grid[row][scol]
        else:
            return 0
    return hap

def barCol(srow, scol):
    hap = 0
    for col in range(scol, scol+BARN):
        if inrange(srow, col):
            hap += grid[srow][col]
        else:
            return 0
    return hap

maxHap = 0
for i in range(n):
    for j in range(m):
        maxHap = max(maxHap, modelTop(i, j), modelLeft(i, j), modelRight(i, j), modelBottom(i, j))
        maxHap = max(maxHap, barCol(i, j), barRow(i, j))

print(maxHap)