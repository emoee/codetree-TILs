x, y = map(int, input().split())

def check(number):
    strNumber = str(number)
    n = len(strNumber)

    c = False
    for i in range(int(n/2)):
        # print(strNumber[i], strNumber[-(i+1)])
        if strNumber[i] == strNumber[-(i+1)]:
            c = True
        else:
            c = False
    
    return c


count = 0
for i in range(x, y+1):
    if check(i):
        count += 1
    
print(count)