y, m, d = map(int, input().split())

leapYear = False
if y%4 == 0 or (y%4==0 and y%100 != 0) or (y%4==0 and y%100==0 and y%400==0):
    leapYear = True

season = ""
if 6 > m > 2:
    season = "Spring"
elif 9 > m > 5:
    season = "Summer"
elif 12 > m > 8:
    season = "Fall"
elif 0 < m < 3 or 11 < m < 13:
    season = "Winter"
else:
    season = -1

days = []
if leapYear:
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days[m] < d:
        season = -1
else:
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days[m] < d:
        season = -1

print(season)