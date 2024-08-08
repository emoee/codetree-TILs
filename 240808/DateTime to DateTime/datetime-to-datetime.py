d, h, m  = map(int, input().split())

ld, lh, lm = 11, 11, 11
result = 0
while 1:
    if ld == d and lh == h and lm == m:
        break
    
    lm += 1
    result += 1
    if lm == 60:
        lh += 1
        lm = 0
    
    if lh == 24:
        ld += 1
        lh = 0

print(result)