n = int(input())

board = [''] * 101

number = 0
for i in range(n):
    p, c = map(str, input().split())
    p = int(p)

    board[p] = c
    number = max(number, p)

maxValue = 0
for i in range(number+1):
    for j in range(i, number+1):
        countG = 0
        countH = 0
        if board[i] != '' and board[j] != '':
            for k in range(i, j+1):
                if board[k] == 'G':
                    countG += 1
                elif board[k] == 'H':
                    countH += 1

            if (countG != 0 and countH != 0) and countG == countH:
                maxValue = max(maxValue, (j-i))
            elif countG > 0 and countH == 0:
                maxValue = max(maxValue, (j-i))
            elif countH > 0 and countG == 0:
                maxValue = max(maxValue, (j-i))

print(maxValue)