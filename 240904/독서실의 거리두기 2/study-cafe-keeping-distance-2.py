n = int(input())
seat = list(input())

def findMax(seat):
    distance = 0
    x, y = 1000, 1000
    for i in range(n-1):
        for j in range(i+1, n):
            if seat[i] == '0' and i == 0 and seat[j] == '1':
                distance = (j-i)
                x, y = i, j
                break

            if seat[i] == '1' and seat[j] == '1':
                if x == 0 and seat[x] == '0' and distance < ((j-i)//2):
                    distance = (j-i)
                    x, y = i, j
                elif x == 0 and seat[x] == '0' and distance > ((j-i)//2):
                    break
                elif distance < (j-i):
                    distance = max(distance, j-i)
                    x, y = i, j
                break

            if seat[i] == '1' and j == n-1 and seat[j] == '0':
                if x == 0 and seat[x] == '0' and distance < (j-i):
                    distance = max(distance, j-i)
                    x, y = i, j
                if x == 0 and seat[x] == '0' and distance > (j-i):
                    break
                elif distance//2 < (j-i):
                    distance = (j-i)
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
# print(d, a, b)
if a == 0 and seat[a] == '0':
    seat[a] = '1'
elif b == n-1 and seat[b] == '0':
    seat[b] = '1'
else:
    seat[(a+b)//2] = '1'
# print("".join(map(str,seat)))

cd, ca, cb = findMin(seat)
print(cd)