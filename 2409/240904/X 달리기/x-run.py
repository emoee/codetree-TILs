x = int(input())

time = 1
position = 0
speed = 1

def getSpeed(current):
    if current == 1:
        return 1
    else:
        return current + getSpeed(current-1)

while True:
    time += 1

    if getSpeed(speed+1) <= x-position:
        speed += 1
    elif getSpeed(speed) <= x-position:
        speed = speed
    else:
        speed -= 1

    position += speed

    if position == x:
        break
print(time)