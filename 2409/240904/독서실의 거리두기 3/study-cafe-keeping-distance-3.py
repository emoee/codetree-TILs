n = int(input())
seat = list(input())

def findMax(seat):
    distance = 0
    x, y = 0, 0
    for i in range(n-1):
        for j in range(i+1, n):
            if seat[i] == '1' and seat[j] == '1':
                if distance < (j-i):
                    distance = max(distance, j-i)
                    x, y = i, j
                break
    return distance, x, y

def findMin(seat):
    distance = 1000
    x, y = 0, 0
    for i in range(n-1):
        for j in range(i+1, n):
            if seat[i] == '1' and seat[j] == '1':
                if distance > (j-i):
                    distance = min(distance, j-i)
                    x, y = i, j
                break
    return distance, x, y

d, a, b = findMax(seat)
seat[(a+b)//2] = '1'
cd, ca, cb = findMin(seat)

print(cd)