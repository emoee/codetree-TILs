n, m = map(int, input().split())

line = [
    int(input()) for _ in range(n)
]
bline = [0]*n

endArray = n
blank = 0

def down(bline, line, endArray, blank):
    for i in range(endArray):
        if line[i] != 0 :
            bline[blank] = line[i]
            blank += 1
    
    endArray = blank
    blank = 0
    return bline, line, endArray, blank

start = 0
for i in range(1, n):
    check = line[start]
    count = 0
    for j in range(start, endArray):
        if line[j] == check:
            count += 1
        else:
            break
    
    if count >= m:
        for j in range(count):
            line[start+j] = 0
        bline, line, endArray, blank = down(bline, line, endArray, blank)
        line = bline
        start = 0
    else:
        start += 1
    count = 0

count = 0
for i in range(n):
    if line[i] != 0:
        count += 1
    else:
        break

print(count)
for i in range(count):
    print(line[i])