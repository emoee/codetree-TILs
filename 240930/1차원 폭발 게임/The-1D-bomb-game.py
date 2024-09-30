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

def bomb(line, endArray):
    loop = False
    for i in range(n):
        check = line[i]
        count = 0
        for j in range(i, endArray):
            if line[j] == check:
                count += 1
            else:
                break
        
        if count >= m:
            loop = True
            for j in range(count):
                line[i+j] = 0
    return line, loop

while True:
    line, loop = bomb(line, endArray)
    bline, line, endArray, blank = down(bline, line, endArray, blank)
    line = bline
    # print(line, endArray)
    if loop == False:
        break

print(endArray)
for i in range(endArray):
    print(line[i])