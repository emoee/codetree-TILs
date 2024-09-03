n = int(input())
seat = list(input())

def findMax(seat):
    distance = 0
    x, y = 0, 0
    for i in range(n-1):
        for j in range(i+1, n):
            if seat[i] == '1' and (j == n-1 and seat[j] == '0'):
                if distance//2 < (j-i):
                    distance = max(distance, j-i)
                    x, y = i, j
                break
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
            if seat[i] == '1' and (j == n and seat[j] == '0'):
                if distance > (j-i):
                    distance = min(distance, j-i)
                    x, y = i, j
                break
            if seat[i] == '1' and seat[j] == '1':
                if distance > (j-i):
                    distance = min(distance, j-i)
                    x, y = i, j
                break
    return distance, x, y

d, a, b = findMax(seat)
if b == n-1:
    seat[b] = '1'
else:
    seat[(a+b)//2] = '1'
cd, ca, cb = findMin(seat)

print(cd)