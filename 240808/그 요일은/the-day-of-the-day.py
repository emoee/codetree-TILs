m1, d1, m2, d2 = map(int, input().split())
day = input()
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
d, n, result = 0, 0, 0

for i, w in enumerate(week):
    if w == day:
        d = i

while True:
    if m1 == m2 and d1 == d2:
        break

    d1 += 1
    n = (n+1)%7

    if d == n:
        result += 1

    if d1 == months[m1]:
        m1 += 1
        d1 = 1
        n = (n+1)%7

        if d == n:
            result += 1

print(result)