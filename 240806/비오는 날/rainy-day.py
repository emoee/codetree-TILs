n = int(input())

data = [
    weather for weather in (tuple(map(str, input().split())) for _ in range(n))
    if weather[-1] == "Rain"
]
data.sort()
date, day, w = data[0]
print(date, day, w)