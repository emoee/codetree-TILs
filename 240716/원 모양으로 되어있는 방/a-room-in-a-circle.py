import sys
n = int(input())
room = []
for i in range(n):
    room.append(int(input()))

minValue = sys.maxsize

for c in range(len(room)):
    sumValue = 0
    for i in range(len(room)):
        sumValue += ((c+i)%n)*room[i]
 
    minValue = min(minValue, sumValue)

print(minValue)