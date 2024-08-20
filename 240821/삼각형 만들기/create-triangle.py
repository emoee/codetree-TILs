n = int(input())
board = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = board[i]
            x2, y2 = board[j]
            x3, y3 = board[k]

            if x1 == x2 and (y1 == y3 or y2 == y3):
                a = area(x1, y1, x2, y2, x3, y3)
                result = max(result, a)
            if x2 == x3 and (y2 == y1 or y1 == y3):
                a = area(x1, y1, x2, y2, x3, y3)
                result = max(result, a)
            if x1 == x3 and (y1 == y2 or y2 == y3):
                a = area(x1, y1, x2, y2, x3, y3)
                result = max(result, a)

print(int(result * 2))