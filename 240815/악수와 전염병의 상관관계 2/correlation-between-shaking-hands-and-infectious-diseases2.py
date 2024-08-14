N, K, P, T = map(int, input().split())

person = [0] * (N)
person[P - 1] = 1
time = []

for i in range(T):
    t, x, y = map(int, input().split())
    time.append([t, x - 1, y - 1])
    
time.sort()
infect = [False] * N
infect[P - 1] = True

for k in range(K):
    t, x, y = time[k]
    if infect[x] or infect[y]:
        infect[x] = True
        infect[y] = True

print("".join(map(str, map(int, infect))))