import sys
n = int(input())

board = []
for i in range(n):
    board.append(tuple(map(int, input().split())))

minValue = sys.maxsize
for check in range(1, n-1):
    sumValue = 0
    index = 0
    for i in range(1, n):
        if check == i:
            continue
        x, y = board[index]
        nx, ny = board[i]

        sumValue += abs(x-nx) + abs(y-ny)

        index = i

    minValue = min(minValue, sumValue)


print(minValue)