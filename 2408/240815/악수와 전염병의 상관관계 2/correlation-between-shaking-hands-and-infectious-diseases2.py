N, K, P, T = map(int, input().split())

infect = [False] * N
infect[P - 1] = True

# 악수 기록 입력
time = []
for _ in range(T):
    t, x, y = map(int, input().split())
    time.append([t, x - 1, y - 1])

time.sort()
shakes = [0] * N
for i in range(T):
    t, x, y = time[i]
    if infect[x]:
        shakes[x] += 1
    if infect[y]:
        shakes[y] += 1
    
    if shakes[x] <= K and infect[x]:
        infect[y] = True
    if shakes[y] <= K and infect[y]:
        infect[x] = True


print("".join(map(str, map(int, infect))))