m1, d1, m2, d2 = map(int, input().split())

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
while True:
    if m1 == m2 and d1 == d2:
        break

    if m1 < m2 or (m1 == m2 and  d1 < d2):
        d1 += 1
        day = (day+1)%7
        if d1 == months[m1]:
            m1 += 1
            d1 = 1
            day = (day+1)%7
    else:
        day = (day-1)%7
        d1 -= 1
        if d1 == months[m1]:
            m1 -= 1
            d1 = 1
            day = (day-1)%7

print(days[day])